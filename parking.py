"""Evaluasi klasifikasi okupansi empat petak PKLot UFPR04."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import cv2
import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_recall_fscore_support
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

SIZE = (960, 540)
THRESHOLDS = (15, 25, 35)
OCCUPANCIES = (0.10, 0.20, 0.30)
CLASS_NAMES = ("Kosong", "Terisi mobil")
SCENARIOS = {
    "baseline": (False, False, False),
    "klasik_lengkap": (True, True, True),
    "tanpa_normalisasi": (False, True, True),
    "tanpa_canny": (True, False, True),
    "tanpa_morfologi": (True, True, False),
}
HOG = cv2.HOGDescriptor((64, 64), (16, 16), (8, 8), (8, 8), 9)


def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def normalize(gray, region):
    low, high = np.percentile(gray[region], (5, 95))
    if high <= low:
        return gray.copy()
    return np.clip((gray.astype(np.float32) - low) * 255 / (high - low), 0, 255).astype(np.uint8)


def mask_for(points):
    points = np.round(np.asarray(points) * SIZE).astype(np.int32)
    mask = np.zeros(SIZE[::-1], np.uint8)
    cv2.fillPoly(mask, [points], 1)
    if not mask.any():
        raise ValueError("Poligon kosong.")
    return mask.astype(bool), points


def feature(gray, mask):
    y, x = np.where(mask)
    pixels = gray.copy()
    pixels[~mask] = int(np.median(pixels[mask]))
    patch = pixels[y.min():y.max()+1, x.min():x.max()+1]
    patch = cv2.resize(patch, (64, 64), interpolation=cv2.INTER_AREA)
    return HOG.compute(patch).ravel()


def classical_stages(gray, reference, region, parameters, threshold):
    use_normalize, use_canny, use_morphology = parameters
    current = normalize(gray, region) if use_normalize else gray
    empty = normalize(reference, region) if use_normalize else reference
    difference = cv2.absdiff(current, empty)
    changes = (difference > threshold).astype(np.uint8)
    new_edges = np.zeros_like(changes)
    kernel = np.ones((3, 3), np.uint8)
    if use_canny:
        edges = cv2.Canny(current, 50, 150)
        old_edges = cv2.dilate(cv2.Canny(empty, 50, 150), kernel)
        new_edges = cv2.dilate(((edges > 0) & (old_edges == 0)).astype(np.uint8), kernel)
    combined = changes | new_edges
    final = combined
    if use_morphology:
        final = cv2.morphologyEx(final, cv2.MORPH_OPEN, kernel)
        final = cv2.morphologyEx(final, cv2.MORPH_CLOSE, kernel)
    return current, difference, changes, new_edges, combined, final


def scores(labels, predictions):
    matrix = confusion_matrix(labels, predictions, labels=[0, 1])
    return dict(
        macro_f1=float(f1_score(labels, predictions, labels=[0, 1], average="macro", zero_division=0)),
        accuracy=float(accuracy_score(labels, predictions)),
        kosong_dibaca_mobil=int(matrix[0, 1]),
        mobil_dibaca_kosong=int(matrix[1, 0]),
    )


def run(root, output):
    root, output = Path(root), Path(output)
    manifest = json.loads((root / "data/manifest.json").read_text())
    manifest_digest = hashlib.sha256((root / "data/manifest.json").read_bytes()).hexdigest()
    slots = [str(slot) for slot in manifest["slots"]]
    dates = {part: {frame["date"] for frame in manifest["frames"] if frame["split"] == part}
             for part in ("dev", "test")}
    calibration = {frame["date"] for frame in manifest["references"].values()}
    if dates["dev"] & dates["test"] or calibration & (dates["dev"] | dates["test"]):
        raise ValueError("Tanggal kalibrasi, pengembangan, dan uji harus terpisah.")
    output.mkdir(parents=True, exist_ok=True)

    cache = {}
    all_frames = list(manifest["references"].values()) + manifest["frames"]
    for frame in all_frames:
        path = root / frame["local"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != frame["sha256"]:
            raise ValueError(f"Checksum citra berubah: {path}")
        if frame["local"] not in cache:
            image = cv2.imread(str(path))
            if image is None:
                raise ValueError(f"Gagal membaca {path}")
            cache[frame["local"]] = cv2.resize(image, SIZE, interpolation=cv2.INTER_AREA)
    masks, polygons, references = {}, {}, {}
    for slot in slots:
        frame = manifest["references"][slot]
        if frame["spaces"][slot]["label"] != 0:
            raise ValueError(f"Acuan petak {slot} terisi.")
        masks[slot], polygons[slot] = mask_for(frame["spaces"][slot]["polygon"])
        references[slot] = cv2.cvtColor(cache[frame["local"]], cv2.COLOR_BGR2GRAY)
    region = np.logical_or.reduce(list(masks.values()))

    review_path = root / "data/review_mobil.csv"
    if not review_path.is_file():
        raise FileNotFoundError("Periksa jenis kendaraan pada review_mobil.csv terlebih dahulu.")
    with review_path.open() as handle:
        review_rows = list(csv.DictReader(handle))
    review = {(row["citra"], row["petak"]): row["verifikasi"] for row in review_rows}
    if len(review) != len(review_rows):
        raise ValueError("Ada baris kurasi ganda.")
    for frame in all_frames:
        checked_slots = [slot for slot in slots if slot in frame["spaces"]]
        # Citra acuan boleh juga digunakan untuk acuan petak lain dari tanggal yang sama.
        for slot in checked_slots:
            required = "mobil" if frame["spaces"][slot]["label"] else "kosong"
            if review.get((frame["local"], slot)) != required:
                raise ValueError(f"Verifikasi petak tidak konsisten: {frame['local']} / {slot}")

    examples = []
    for frame in manifest["frames"]:
        gray = cv2.cvtColor(cache[frame["local"]], cv2.COLOR_BGR2GRAY)
        for slot in slots:
            label = frame["spaces"][slot]["label"]
            examples.append(dict(frame=frame, slot=slot, label=label, features=feature(gray, masks[slot])))
    indices = {part: np.array([i for i, e in enumerate(examples) if e["frame"]["split"] == part])
               for part in ("dev", "test")}
    labels = np.array([e["label"] for e in examples])
    for part, ix in indices.items():
        if len(np.unique(labels[ix])) != 2:
            raise ValueError(f"Kedua kelas harus terwakili di {part}.")

    # Rasio per kandidat ambang. Label uji tidak dipakai pada langkah ini.
    ratios = {}
    for scenario, parameters in SCENARIOS.items():
        values = []
        for frame in manifest["frames"]:
            gray = cv2.cvtColor(cache[frame["local"]], cv2.COLOR_BGR2GRAY)
            per_slot = {slot: [] for slot in slots}
            for slot in slots:
                for threshold in THRESHOLDS:
                    stages = classical_stages(gray, references[slot], region, parameters, threshold)
                    per_slot[slot].append(float(stages[-1][masks[slot]].mean()))
            values.extend(per_slot[slot] for slot in slots)
        ratios[scenario] = np.asarray(values)

    tuned = {}
    for scenario in ("baseline", "klasik_lengkap"):
        candidates = []
        for column, threshold in enumerate(THRESHOLDS):
            for occupancy in OCCUPANCIES:
                pred = ratios[scenario][indices["dev"], column] >= occupancy
                candidates.append((scores(labels[indices["dev"]], pred)["macro_f1"], column, occupancy))
        # Urutan kandidat memutus tie secara deterministik.
        score, column, occupancy = max(candidates, key=lambda x: x[0])
        tuned[scenario] = dict(difference_threshold=THRESHOLDS[column], occupancy_threshold=occupancy,
                               dev_macro_f1=score)
    for scenario in ("tanpa_normalisasi", "tanpa_canny", "tanpa_morfologi"):
        tuned[scenario] = {key: tuned["klasik_lengkap"][key]
                           for key in ("difference_threshold", "occupancy_threshold")}
        tuned[scenario]["inherited_from"] = "klasik_lengkap"
    predictions = {}
    for scenario in SCENARIOS:
        column = THRESHOLDS.index(tuned[scenario]["difference_threshold"])
        predictions[scenario] = (ratios[scenario][indices["test"], column]
                                  >= tuned[scenario]["occupancy_threshold"]).astype(int)

    features = np.stack([e["features"] for e in examples])
    model = make_pipeline(StandardScaler(), LinearSVC(C=1.0, class_weight="balanced", random_state=42,
                                                      max_iter=20000))
    model.fit(features[indices["dev"]], labels[indices["dev"]])
    predictions["hog_svm"] = model.predict(features[indices["test"]])
    joblib.dump(dict(model=model, polygons=polygons, work_size=SIZE, classes=CLASS_NAMES,
                     manifest_sha256=manifest_digest), output / "hog_svm.joblib")
    test_labels = labels[indices["test"]]
    baseline_f1 = scores(test_labels, predictions["baseline"])["macro_f1"]
    full_f1 = scores(test_labels, predictions["klasik_lengkap"])["macro_f1"]
    summaries, details, weather_rows = [], [], []
    fig, axes = plt.subplots(2, 3, figsize=(11, 7), constrained_layout=True)
    for ax, (scenario, pred) in zip(axes.flat, predictions.items()):
        metric = scores(test_labels, pred)
        summaries.append(dict(skenario=scenario, observasi=len(pred),
                             **metric, selisih_terhadap_baseline=metric["macro_f1"]-baseline_f1,
                             selisih_terhadap_lengkap=metric["macro_f1"]-full_f1))
        matrix = confusion_matrix(test_labels, pred, labels=[0, 1])
        ax.imshow(matrix, cmap="Blues", vmin=0, vmax=len(pred))
        for (y, x), value in np.ndenumerate(matrix):
            ax.text(x, y, str(value), ha="center", va="center", fontsize=15)
        ax.set(xticks=[0,1], yticks=[0,1], xticklabels=["Kosong","Mobil"],
               yticklabels=["Kosong","Mobil"], xlabel="Prediksi", ylabel="Acuan",
               title=f"{scenario}\nMacro-F1 {metric['macro_f1']:.3f}")
        precision, recall, f1, support = precision_recall_fscore_support(test_labels, pred,
                                                                       labels=[0,1], zero_division=0)
        for c in (0,1):
            details.append(dict(skenario=scenario,kelas=CLASS_NAMES[c],precision=float(precision[c]),
                                recall=float(recall[c]),f1=float(f1[c]),support=int(support[c])))
        for weather in sorted({e["frame"]["weather"] for e in examples}):
            subset = [j for j,i in enumerate(indices["test"]) if examples[i]["frame"]["weather"] == weather]
            if subset:
                weather_rows.append(dict(skenario=scenario,cuaca=weather,observasi=len(subset),
                    kelas_kosong=int((test_labels[subset]==0).sum()),
                    kelas_mobil=int((test_labels[subset]==1).sum()),**scores(test_labels[subset], pred[subset])))
    fig.suptitle("PKLot UFPR04 asli · Empat petak · Tanggal uji terpisah")
    fig.savefig(output / "confusion_matrix.png", dpi=160)
    plt.close(fig)
    write_csv(output / "metrik.csv", summaries)
    write_csv(output / "metrik_per_kelas.csv", details)
    write_csv(output / "metrik_per_cuaca.csv", weather_rows)
    records = []
    for j,i in enumerate(indices["test"]):
        e=examples[i]
        records.append(dict(citra=e["frame"]["local"],tanggal=e["frame"]["date"],
                            cuaca=e["frame"]["weather"],petak=e["slot"],label=e["label"],
                            **{name:int(pred[j]) for name,pred in predictions.items()}))
    write_csv(output / "prediksi_uji.csv", records)
    (output / "parameter.json").write_text(json.dumps(dict(thresholds=tuned, svm_C=1.0,
                      source="PKLot UFPR04 via Voxel51", manifest_sha256=manifest_digest,
                      dev_dates=sorted(dates["dev"]),test_dates=sorted(dates["test"]),
                      calibration_dates=sorted(calibration)),indent=2))

    # Satu contoh dipilih dari foto uji pertama sebelum melihat keberhasilan prediksi.
    frame = next(e["frame"] for e in examples if e["frame"]["split"] == "test")
    image = cache[frame["local"]].copy()
    for slot in slots:
        row = next(row for row in records if row["citra"]==frame["local"] and row["petak"]==slot)
        color=(30,30,230) if row["hog_svm"] else (0,200,0)
        cv2.polylines(image,[polygons[slot]],True,color,2)
        x,y=polygons[slot].min(axis=0)
        cv2.putText(image,f"{slot}: {'Mobil' if row['hog_svm'] else 'Kosong'}",(int(x),int(y)),
                    cv2.FONT_HERSHEY_SIMPLEX,0.4,color,1,cv2.LINE_AA)
    cv2.imwrite(str(output / "contoh_prediksi_svm.png"),image)
    slot=slots[0]
    gray=cv2.cvtColor(cache[frame["local"]],cv2.COLOR_BGR2GRAY)
    stages=classical_stages(gray,references[slot],region,SCENARIOS["klasik_lengkap"],
                            tuned["klasik_lengkap"]["difference_threshold"])
    fig,axes=plt.subplots(2,4,figsize=(13,6),constrained_layout=True)
    shown=[("Foto uji",cv2.cvtColor(cache[frame["local"]],cv2.COLOR_BGR2RGB)),
           ("Acuan petak "+slot,references[slot]),
           *zip(["Normalisasi","Selisih","Mask selisih","Tepi baru","OR","Morfologi"],stages)]
    for ax,(title,image) in zip(axes.flat,shown):
        ax.imshow(image,cmap="gray");ax.set_title(title);ax.axis("off")
    fig.suptitle("Tahapan pada data asli · "+Path(frame["local"]).name)
    fig.savefig(output / "tahapan.png",dpi=140);plt.close(fig)
    print(json.dumps(summaries,indent=2))
    return summaries


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument("--output",type=Path,default=None)
    args=parser.parse_args()
    run(args.root,args.output or args.root/"results")
