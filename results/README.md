# Hasil evaluasi

Folder ini berisi keluaran pengujian data asli per **25 November 2026**. Raisya memeriksa tabel dan pembahasannya, Govin memeriksa mask serta tahapan, dan Marvin menggunakan model untuk aplikasi demo.

File pada folder ini sudah tersimpan di GitHub. Untuk melihat hasil, buka tautan di bawah tanpa menjalankan notebook. Hasil demo sintetis Minggu 12 tersedia terpisah pada [folder hasil Minggu 12](../progres/minggu12/hasil/).

## File yang dibuka

| Keperluan | File |
|---|---|
| Membandingkan enam skenario | [metrik.csv](metrik.csv) |
| Memeriksa precision, recall, dan F1 tiap kelas | [metrik_per_kelas.csv](metrik_per_kelas.csv) |
| Membaca hasil menurut cuaca | [metrik_per_cuaca.csv](metrik_per_cuaca.csv) |
| Menelusuri prediksi setiap foto dan petak | [prediksi_uji.csv](prediksi_uji.csv) |
| Memeriksa parameter evaluasi | [parameter.json](parameter.json) |
| Melihat kesalahan dalam confusion matrix | [confusion_matrix.png](confusion_matrix.png) |
| Melihat contoh status empat petak | [contoh_prediksi_svm.png](contoh_prediksi_svm.png) |
| Memeriksa tahapan metode klasik | [tahapan.png](tahapan.png) |
| Melihat enam kasus gagal SVM | [kasus_gagal_svm.png](kasus_gagal_svm.png) |
| Memakai model SVM yang sudah dilatih | [hog_svm.joblib](hog_svm.joblib) |

## Cara membaca

Semua skenario memakai 144 observasi uji yang sama. Pada `prediksi_uji.csv`, label **0 berarti kosong** dan **1 berarti terisi mobil**. Pada confusion matrix, baris menunjukkan label acuan dan kolom menunjukkan prediksi.

Nilai acuan saat ini: macro-F1 baseline **0,8579**, metode klasik lengkap **0,4696**, dan HOG + SVM **0,9569**. SVM benar pada 138 dari 144 observasi; enam mobil terbaca kosong. Metode klasik lengkap salah menandai 51 petak kosong sebagai terisi.

Tabel per cuaca dibaca dengan jumlah sampelnya. Kondisi hujan hanya memiliki tiga foto uji atau 12 observasi petak.

## Pemeriksaan dan percobaan berikutnya

Raisya mencocokkan jumlah kesalahan di tabel prediksi dengan metrik dan confusion matrix, lalu menulis pembahasan pada [laporan evaluasi](../progres/minggu13/laporan_evaluasi.md). Govin memakai gambar tahapan untuk menelusuri kegagalan metode klasik. Tugas terperinci ada di [progres Minggu 13](../progres/minggu13/README.md).

`parking.py` menghasilkan tabel metrik, prediksi, parameter, model SVM, confusion matrix, contoh prediksi, dan gambar tahapan. Gambar `kasus_gagal_svm.png` merupakan visualisasi tambahan yang sudah disiapkan; gambar ini tidak dibuat ulang oleh perintah tersebut.

Untuk mencoba perubahan, gunakan `python parking.py --output hasil_percobaan` dari folder utama. Catat konfigurasi dan hasilnya terpisah. Hasil 25 November sudah dilihat tim; perbaikan berdasarkan hasil tersebut perlu dinyatakan sebagai iterasi setelah pengujian, dengan pemisahan uji baru untuk penilaian berikutnya.

Model `hog_svm.joblib` digunakan bersama proses ekstraksi fitur HOG dan praproses di `parking.py`. Model tersebut belum berupa aplikasi yang menerima sembarang foto parkir.

[Kembali ke halaman utama](../README.md)
