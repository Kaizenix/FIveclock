# Progres Minggu 13
23–27 November 2026 · Pembaruan 25 November

Minggu ini pekerjaan sudah masuk ke pengujian PKLot asli. Saya rangkum hasilnya di sini supaya bagian data, implementasi, dan analisis bisa diperiksa bersama.

## Hasil sampai 25 November

Data yang tersedia berjumlah 64 foto dari kamera UFPR04. Empat foto digunakan sebagai acuan kosong, 24 foto untuk pengembangan, dan 36 foto untuk pengujian. Empat petak diperiksa pada tiap foto uji sehingga ada 144 observasi. Tanggal kalibrasi, pengembangan, dan pengujian sudah dipisahkan.

| Skenario | Macro-F1 |
|---|---:|
| Baseline | 0,8579 |
| Metode klasik lengkap | 0,4696 |
| Tanpa normalisasi | 0,7941 |
| Tanpa Canny | 0,6898 |
| Tanpa morfologi | 0,4696 |
| HOG + SVM linear | 0,9569 |

SVM menghasilkan 138 prediksi benar dari 144 observasi. Enam petak yang berisi mobil terbaca kosong. Metode klasik lengkap masih salah membaca 51 petak kosong sebagai terisi. Target macro-F1 0,85 untuk metode klasik lengkap belum tercapai.

## Bukti hasil minggu ini

| Hasil | File yang diperiksa | Status per 25 November |
|---|---|---|
| Data asli, label, dan pembagian tanggal | [Manifest](../../data/manifest.json), [panduan data](../../data/README.md) | Tersedia; pemeriksaan ulang anggota masih perlu dicatat |
| Kode enam skenario | [parking.py](../../parking.py), [notebook evaluasi](../../Fiveclock_Evaluasi_25_November.ipynb) | Sudah dijalankan |
| Perbandingan nilai enam skenario | [metrik.csv](../../results/metrik.csv) | Tersedia |
| Prediksi tiap foto dan petak | [prediksi_uji.csv](../../results/prediksi_uji.csv) | Tersedia, 144 observasi uji |
| Metrik per kelas dan cuaca | [Per kelas](../../results/metrik_per_kelas.csv), [per cuaca](../../results/metrik_per_cuaca.csv) | Tersedia |
| Confusion matrix dan contoh prediksi | Gambar di bawah | Tersedia |
| Tahapan dan kasus gagal | [Tahapan metode](../../results/tahapan.png), [kasus gagal SVM](../../results/kasus_gagal_svm.png) | Tersedia |
| Model HOG + SVM | [hog_svm.joblib](../../results/hog_svm.joblib) | Sudah dilatih |
| Pembahasan evaluasi | [Laporan evaluasi](laporan_evaluasi.md) | Draf tersedia; pemeriksaan anggota masih berjalan |
| Aplikasi demo | Target Marvin pada tabel tugas | Belum tersedia |

### Confusion matrix

![Confusion matrix enam skenario pada 144 observasi uji](../../results/confusion_matrix.png)

### Contoh prediksi

![Contoh prediksi HOG dan SVM pada empat petak](../../results/contoh_prediksi_svm.png)

## Pembagian tugas sampai 27 November

Hasil pengujian awal sudah tersedia. Bagian berikut menjadi tanggung jawab pemeriksaan dan pengembangan tiap anggota.

| Anggota | Pekerjaan | File yang dibuka | Target hasil |
|---|---|---|---|
| Ardan | Menyatukan progres, menyesuaikan proposal dengan implementasi, dan menyiapkan bahan asistensi | README.md, laporan_evaluasi.md, dan proposal | Catatan progres yang konsisten dan daftar kendala |
| Cikal | Memeriksa ulang kurasi serta pembagian data | data/contact_0.jpg sampai contact_7.jpg, data/review_mobil.csv, dan data/manifest.json | Catatan koreksi label atau konfirmasi data |
| Govin | Menelusuri penyebab salah deteksi pada metode lengkap | parking.py dan results/tahapan.png | Contoh mask bermasalah beserta penjelasannya |
| Raisya | Memeriksa skor dan membahas hasil ablasi | results/metrik.csv, results/prediksi_uji.csv, dan results/confusion_matrix.png | Draf analisis hasil dan kasus gagal |
| Marvin | Menghubungkan prediksi dengan aplikasi demo | parking.py dan results/hog_svm.joblib | Prototipe yang menampilkan status empat petak |

## Kendala

Normalisasi dan penambahan tepi dengan OR belum memberikan perbaikan pada konfigurasi yang diuji. Hasil tanpa normalisasi dan tanpa Canny justru lebih tinggi daripada metode lengkap. Ini perlu dijelaskan dari gambar mask dan pola salah deteksinya.

Kurasi awal sudah tersedia. Pemeriksaan ulang anggota terhadap data dan hasil masih menjadi pekerjaan minggu ini.

## Lanjutan

Setelah pemeriksaan hasil selesai, pekerjaan diteruskan ke aplikasi demo, penyusunan bab hasil, slide, dan video. Jika metode diubah setelah hasil uji ini dilihat, percobaan berikutnya perlu dicatat sebagai iterasi baru.

[Laporan evaluasi lengkap](laporan_evaluasi.md)  
[Notebook evaluasi](../../Fiveclock_Evaluasi_25_November.ipynb)
