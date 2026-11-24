# Progres Minggu 11
9–13 November 2026

Saya pakai minggu ini untuk merapikan arah proyek dan isi proposal. Fokusnya mendeteksi status petak parkir mobil dari foto kamera tetap. Data yang dipakai adalah PKLot, khususnya UFPR04.

## Hasil pekerjaan

Draf proposal sudah memuat latar belakang, rumusan masalah, tujuan, penelitian terkait, dan rencana percobaan. Baseline yang disiapkan memakai selisih grayscale terhadap foto acuan saat petak kosong. Metode lengkap menambahkan normalisasi pencahayaan, deteksi tepi, dan morfologi.

Rencana datanya 24 foto pengembangan dan 36 foto uji. Pembagian tanggal dibuat terpisah supaya foto uji berasal dari hari yang berbeda dengan data pengembangan. Penilaian memakai macro-F1, confusion matrix, dan tiga ablasi.

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
