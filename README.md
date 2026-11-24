# Fiveclock Evaluasi Parkir Mobil

Evaluasi dan ablasi per 25 November 2026 pada PKLot UFPR04 asli. Keenam skenario dijalankan pada 36 foto uji dengan empat petak per foto. Hasil terperinci ada pada Laporan_Progres_25_November.md.

| Metode | Macro-F1 |
|---|---:|
| Baseline selisih citra | 0,8579 |
| Klasik lengkap | 0,4696 |
| Tanpa normalisasi | 0,7941 |
| Tanpa Canny | 0,6898 |
| Tanpa morfologi | 0,4696 |
| HOG + SVM linear | 0,9569 |

Target macro-F1 0,85 untuk metode klasik lengkap belum tercapai. Data uji memiliki 56 petak kosong dan 88 petak berisi mobil. HOG + SVM benar pada 138 dari 144 observasi.

## Menjalankan lokal

Disarankan Python 3.11 atau 3.12.

    python -m pip install -r requirements.txt
    python parking.py

Semua hasil diekspor ke results, termasuk confusion matrix, tabel prediksi, metrik per kelas dan cuaca, serta model SVM.

## Isi paket

- parking.py merupakan implementasi yang digunakan untuk menghasilkan hasil.
- Fiveclock_Evaluasi_25_November.ipynb adalah notebook dengan keluaran evaluasi asli.
- data/images memuat 64 foto sumber.
- data/manifest.json memuat checksum, pembagian tanggal, label, dan poligon.
- data/review_mobil.csv memuat pemeriksaan visual oleh asisten AI.
- data/contact_0.jpg sampai contact_7.jpg memperlihatkan crop untuk peninjauan tim.
- data/source.json mencatat sumber dan revisi mirror.
- results memuat hasil keenam skenario dan model SVM.
- PROGRES_M13.txt dapat disesuaikan untuk isian tab progres.

## Protokol

Kalibrasi, pengembangan, dan pengujian memakai tanggal berbeda. Pengembangan 24 foto dipakai untuk penalaan ambang dan pelatihan SVM. Tiga ablasi memakai parameter metode klasik lengkap. Label uji digunakan untuk menghitung metrik. Canny diimplementasikan melalui OpenCV 4.11, sementara fitur HOG menggunakan HOGDescriptor OpenCV.

Foto bersumber dari PKLot melalui mirror Voxel51. Poligon dan status dikonversi dari format FiftyOne yang berasal dari XML. Data menyasar empat petak mobil. Model memprediksi okupansi petak pada kamera yang dikenal. Pemeriksaan jenis kendaraan dalam paket dilakukan secara visual oleh asisten AI.

## Lisensi data

Foto PKLot berlisensi CC BY 4.0. Rincian atribusi dan perubahan format tersedia pada ATTRIBUTION.md.


## Arsip progres mingguan

- [Minggu 12, 16–20 November — implementasi awal dan uji sintetis](progres/minggu12/README.md)
- [Minggu 13, 25 November — evaluasi PKLot asli dan ablasi](Laporan_Progres_25_November.md)
