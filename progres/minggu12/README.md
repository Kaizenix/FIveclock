# Progres Minggu 12, 16–20 November 2026

Catatan ini ditambahkan setelah evaluasi Minggu 13 tersedia. Periode pada judul menunjukkan tahap pekerjaan yang didokumentasikan. Waktu commit mengikuti waktu unggahan sebenarnya.

## Pekerjaan yang tersedia pada Minggu 12

Implementasi awal membaca pasangan foto dan XML, menetapkan poligon petak, memakai acuan kosong per petak, dan menjalankan normalisasi P5–P95, selisih intensitas, Canny, penggabungan OR, serta opening dan closing. Keluaran mencakup mask setiap tahap, status petak, PNG, dan CSV.

Uji saat itu menggunakan data sintetis untuk memeriksa jalannya program. Dalam contoh tersimpan, dua petak kosong salah diprediksi terisi mobil oleh metode lengkap. Temuan ini menjadi bahan evaluasi normalisasi dan penggabungan mask. Angka tersebut berasal dari contoh sintetis.

Notebook arsip terdapat pada [Fiveclock_Implementasi_M12_Colab.ipynb](Fiveclock_Implementasi_M12_Colab.ipynb). Grafik dapat dihasilkan kembali dengan menjalankan notebook di Colab. Output teks demo disertakan.

## Bagian yang baru dituntaskan pada Minggu 13

Pengambilan subset PKLot asli, pemeriksaan visual petak mobil, pelatihan HOG + SVM, dan evaluasi enam skenario pada 144 observasi dituntaskan pada 25 November 2026. Hasilnya tercatat dalam [laporan evaluasi](../../Laporan_Progres_25_November.md).

## Kontribusi dan asistensi

Kode awal dan uji sintetis dalam arsip ini disiapkan oleh asisten AI. Setiap anggota mencatat pemeriksaan, perubahan kode, analisis, atau integrasi yang benar-benar dikerjakannya. Status asistensi dan pengumpulan Minggu 12 perlu dikonfirmasi melalui tab Progres kelas.
