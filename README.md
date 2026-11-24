# Fiveclock — Deteksi Status Parkir Mobil

Saya gunakan repositori ini untuk mencatat perkembangan proyek fiveclock dan menyatukan pekerjaan anggota. Proyeknya menentukan status petak kosong atau terisi mobil dari citra statis PKLot UFPR04.

## Progres mingguan

| Minggu | Fokus | Catatan |
|---|---|---|
| 11 · 9–13 November | Perencanaan dan proposal | [Hasil, pembagian tugas, dan kendala](progres/minggu11/README.md) |
| 12 · 16–20 November | Implementasi awal | [Hasil, pembagian tugas, dan kendala](progres/minggu12/README.md) |
| 13 · 23–27 November | Evaluasi dan ablasi | [Pembaruan sampai 25 November](progres/minggu13/README.md) |

Pembagian di tiap halaman menjadi pegangan tanggung jawab anggota. Hasil yang sudah tersedia dicatat pada bagian hasil pekerjaan. Pemeriksaan atau pengembangan yang masih perlu dikerjakan dicatat pada tabel tugas dan rencana berikutnya.

## Hasil pengujian terakhir

Enam skenario sudah dijalankan pada 36 foto uji, dengan empat petak per foto. Pembahasan lengkap ada pada [laporan evaluasi](Laporan_Progres_25_November.md).

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

## File proyek

- parking.py merupakan implementasi yang digunakan untuk menghasilkan hasil.
- Fiveclock_Evaluasi_25_November.ipynb adalah notebook dengan keluaran evaluasi asli.
- data/images memuat 64 foto sumber.
- data/manifest.json memuat checksum, pembagian tanggal, label, dan poligon.
- data/review_mobil.csv memuat hasil kurasi awal untuk diperiksa kembali oleh bagian data.
- data/contact_0.jpg sampai contact_7.jpg memperlihatkan crop untuk peninjauan tim.
- data/source.json mencatat sumber dan revisi mirror.
- results memuat hasil keenam skenario dan model SVM.
- PROGRES_M13.txt dapat disesuaikan untuk isian tab progres.

## Protokol

Kalibrasi, pengembangan, dan pengujian memakai tanggal berbeda. Pengembangan 24 foto dipakai untuk penalaan ambang dan pelatihan SVM. Tiga ablasi memakai parameter metode klasik lengkap. Label uji digunakan untuk menghitung metrik. Canny diimplementasikan melalui OpenCV 4.11, sementara fitur HOG menggunakan HOGDescriptor OpenCV.

Foto bersumber dari PKLot melalui mirror Voxel51. Poligon dan status dikonversi dari format FiftyOne yang berasal dari XML. Data menyasar empat petak mobil. Model memprediksi okupansi petak pada kamera yang dikenal. Jenis kendaraan diperiksa secara visual pada tahap kurasi awal. Peninjauan ulang anggota dicatat pada progres Minggu 13.

## Lisensi data

Foto PKLot berlisensi CC BY 4.0. Rincian atribusi dan perubahan format tersedia pada ATTRIBUTION.md.
