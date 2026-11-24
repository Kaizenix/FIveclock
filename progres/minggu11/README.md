# Progres Minggu 11
9–13 November 2026

Saya pakai minggu ini untuk merapikan arah proyek dan isi proposal. Fokusnya mendeteksi status petak parkir mobil dari foto kamera tetap. Data yang dipakai adalah PKLot, khususnya UFPR04.

## Hasil pekerjaan

Draf proposal sudah memuat latar belakang, rumusan masalah, tujuan, penelitian terkait, dan rencana percobaan. Baseline yang disiapkan memakai selisih grayscale terhadap foto acuan saat petak kosong. Metode lengkap menambahkan normalisasi pencahayaan, deteksi tepi, dan morfologi.

Rencana datanya 24 foto pengembangan dan 36 foto uji. Pembagian tanggal dibuat terpisah supaya foto uji berasal dari hari yang berbeda dengan data pengembangan. Penilaian memakai macro-F1, confusion matrix, dan tiga ablasi.

## Bukti hasil minggu ini

Hasil tahap perencanaan saya catat di halaman ini. Draf proposal disebut dalam progres, tetapi filenya belum tersedia di repositori.

| Hasil | Lokasi | Status |
|---|---|---|
| Rancangan masukan, proses, dan keluaran | [Rancangan awal](#rancangan-awal) | Tercatat di halaman ini |
| Pembagian tanggung jawab anggota | [Pembagian tugas](#pembagian-tugas) | Tercatat di halaman ini |
| Draf proposal | Belum ada file di repositori | Perlu dilengkapi |
| Hasil pengujian data asli | Dilanjutkan pada Minggu 13 | Belum tersedia pada tahap ini |

### Rancangan awal

| Bagian | Rancangan |
|---|---|
| Masalah | Menentukan apakah petak parkir mobil kosong atau terisi dari foto kamera tetap |
| Masukan | Foto parkir, posisi poligon petak, dan foto acuan kosong bagi tiap petak |
| Baseline | Selisih grayscale terhadap acuan kosong, thresholding, lalu perhitungan rasio piksel aktif |
| Metode lengkap | Normalisasi pencahayaan, selisih citra, deteksi tepi, penggabungan mask, dan morfologi |
| Keluaran | Status tiap petak, jumlah petak kosong, gambar prediksi, dan tabel hasil |
| Pengujian | Pemisahan tanggal pengembangan dan uji, macro-F1, confusion matrix, serta tiga ablasi |

Catatan ini merangkum rancangan tahap awal. Berkas data terpilih dan hasil evaluasi yang tersedia sekarang ditautkan pada Minggu 13.

## Pembagian tugas

Tabel ini menjadi pegangan tanggung jawab tiap anggota pada tahap proposal.

| Anggota | Bagian yang dipegang | Target hasil |
|---|---|---|
| Ardan | Menyatukan isi proposal, menjaga ruang lingkup, dan menyusun jadwal | Draf proposal dan pembagian kerja |
| Cikal | Mempelajari struktur PKLot, anotasi petak, dan sumber data | Rencana pemilihan foto dan penjelasan label |
| Govin | Merancang baseline dan urutan pengolahan citra | Diagram alir serta alasan pemilihan metode |
| Raisya | Menentukan ukuran keberhasilan dan skenario pengujian | Metrik, target, serta rencana ablasi |
| Marvin | Menentukan masukan dan keluaran aplikasi | Rancangan tampilan foto, status petak, dan jumlah kosong |

## Kendala

Pada tahap ini pengujian PKLot asli belum berjalan. Data dan baseline awal masih perlu disiapkan sebelum rancangan metode bisa diperiksa lewat hasil program.

## Lanjutan

Berikutnya saya fokuskan pekerjaan ke implementasi awal. Targetnya membaca foto dan anotasi, memilih petak, lalu menampilkan hasil dari setiap tahap pengolahan.

[Progres Minggu 12](../minggu12/README.md)
