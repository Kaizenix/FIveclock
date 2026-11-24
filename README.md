# Fiveclock — Deteksi Status Slot Parkir Mobil

Repositori tugas besar Pengolahan Citra Digital, kelas RA, topik 2. Saya gunakan halaman ini sebagai pegangan pengerjaan kelompok. Pembaruan terakhir: **25 November 2026**.

Proyek menentukan status kosong atau terisi pada empat petak parkir mobil dari citra statis PKLot UFPR04. Evaluasi data asli sudah berjalan. Pemeriksaan anggota dan aplikasi demo masih dikerjakan.

## Mulai dari sini

| Keperluan | File yang dipakai |
|---|---|
| Melihat tugas anggota dan target minggu ini | [Progres Minggu 13](progres/minggu13/README.md) |
| Menjalankan pengujian lewat Colab | [Notebook evaluasi utama](https://colab.research.google.com/github/Kaizenix/FIveclock/blob/main/Fiveclock_Evaluasi_25_November.ipynb) |
| Mengubah metode atau menjalankan lewat Python | [parking.py](parking.py) |
| Membaca hasil, ablasi, dan keterbatasan | [Laporan evaluasi 25 November](progres/minggu13/laporan_evaluasi.md) |
| Memeriksa sumber, pembagian, dan label data | [Panduan data](data/README.md) |
| Mencari tabel nilai, prediksi, gambar, dan model | [Panduan hasil](results/README.md) |

**Untuk pengerjaan saat ini, gunakan notebook evaluasi di atas.** Notebook di folder Minggu 12 mencatat implementasi awal dengan data sintetis.

## Menjalankan pengujian

### Google Colab

1. Buka tautan notebook evaluasi utama pada tabel.
2. Sambungkan runtime Python dengan CPU.
3. Pilih **Runtime → Run all**. Sel persiapan mengambil repositori beserta data jika belum tersedia.
4. Tunggu enam skenario selesai. Tabel dan gambar hasil akan muncul di notebook; file hasil disimpan di folder `results` dalam runtime.

Keluaran yang sudah terlihat di notebook berasal dari pengujian 25 November. Jalankan ulang untuk menghasilkan keluaran pada runtime sendiri. Jika muncul pesan OpenCV tidak memiliki `HOGDescriptor`, pasang `opencv-python-headless==4.11.0.86`, mulai ulang runtime, lalu jalankan kembali.

### Komputer sendiri

Gunakan Python 3.11 atau 3.12. Jalankan dari folder repositori:

```bash
python -m pip install -r requirements.txt
python parking.py
```

Perintah tersebut menjalankan evaluasi dan menulis ulang hasil yang dihasilkan oleh `parking.py` dalam `results`. Untuk percobaan dengan folder keluaran terpisah:

```bash
python parking.py --output hasil_percobaan
```

## Pegangan tiap anggota

| Anggota | Bagian yang dipegang | Mulai dari |
|---|---|---|
| Ardan — Project Lead | Mengatur pekerjaan, menyatukan progres dan laporan, menyiapkan asistensi | Halaman ini dan [progres minggu ini](progres/minggu13/README.md) |
| Cikal — Data Engineer & Annotator | Memeriksa data, label, acuan kosong, dan pembagian tanggal | [data/README.md](data/README.md) |
| Govin — Computer Vision Engineer | Memeriksa implementasi dan kegagalan metode klasik | [parking.py](parking.py), [gambar tahapan](results/tahapan.png) |
| Raisya — Evaluation & QA Analyst | Memeriksa metrik, ablasi, dan kasus gagal | [results/README.md](results/README.md), [laporan evaluasi](progres/minggu13/laporan_evaluasi.md) |
| Marvin — Application Engineer | Membuat aplikasi demo dari hasil prediksi | [parking.py](parking.py), [model SVM](results/hog_svm.joblib) |

Rincian tugas dan target sampai 27 November ada di progres Minggu 13. Tabel ini menunjukkan penanggung jawab; pekerjaan yang selesai dicatat setelah hasilnya diperiksa. Aplikasi demo belum tersedia di repositori.

## Hasil terakhir

Dari 36 foto uji diperoleh 144 observasi petak. Macro-F1 baseline **0,8579**, metode klasik lengkap **0,4696**, dan HOG + SVM **0,9569**. Target 0,85 untuk metode klasik lengkap belum tercapai. Enam skenario beserta kesalahannya dibahas di [laporan evaluasi](progres/minggu13/laporan_evaluasi.md).

## Urutan pengerjaan

| Minggu | Fokus | Catatan pengerjaan |
|---|---|---|
| 11 · 9–13 November | Perencanaan dan proposal | [Progres Minggu 11](progres/minggu11/README.md) |
| 12 · 16–20 November | Implementasi awal dengan data sintetis | [Progres Minggu 12](progres/minggu12/README.md) |
| 13 · 23–27 November | Evaluasi data asli dan ablasi | [Progres Minggu 13](progres/minggu13/README.md) |

Tahap berikutnya adalah aplikasi demo dan penyusunan laporan akhir, slide, serta video. Batas pengumpulan akhir: **6 Desember 2026, 23.59 WIB**.

Sumber dan lisensi foto dicatat pada [panduan data](data/README.md#sumber-dan-lisensi).
