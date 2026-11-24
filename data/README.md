# Data parkir mobil

Folder ini dipakai Cikal untuk memeriksa data dan label. Data evaluasi saat ini berupa subset PKLot UFPR04: **64 foto asli dan empat petak**, ID 1–4. Foto berasal dari satu kamera.

## File yang dipakai

| File | Isi dan kegunaan |
|---|---|
| [manifest.json](manifest.json) | Daftar foto, checksum, pembagian data, poligon petak, dan label. Dibaca oleh `parking.py`. |
| [images/](images/) | 64 foto sumber yang digunakan dalam evaluasi. |
| [review_mobil.csv](review_mobil.csv) | Catatan kurasi awal per foto dan petak. Kolom pemeriksa menyebut siapa yang melakukan pemeriksaan. |
| [contact_0.jpg](contact_0.jpg)–[contact_7.jpg](contact_7.jpg) | Delapan lembar crop untuk memeriksa seluruh 256 pasangan foto dan petak. |
| [source.json](source.json) | Sumber mirror dan revisi unduhan untuk penelusuran data. |

Label dalam manifest dan hasil prediksi: **0 = kosong**, **1 = terisi mobil**.

## Pembagian data

| Bagian | Tanggal pengambilan | Foto | Kegunaan |
|---|---|---:|---|
| Acuan kosong | 7 Desember 2012 | 4 | Masing-masing foto menjadi acuan kosong bagi satu petak. Petak lain dalam foto tersebut bisa terisi. |
| Pengembangan | 8, 11, 12 Desember 2012 | 24 | Memilih ambang dan melatih HOG + SVM; 96 observasi. |
| Pengujian | 14, 15, 16 Desember 2012 | 36 | Mengukur enam skenario; 144 observasi. |

Tanggal di tabel adalah tanggal foto dataset. Tanggal pengerjaan kelompok dicatat di folder progres.

Data pengembangan berisi 28 observasi kosong dan 68 mobil. Data uji berisi 56 kosong dan 88 mobil. Subset ini belum mencakup seluruh PKLot.

## Pemeriksaan minggu ini

1. Buka contact sheet, lalu cocokkan foto dan ID petak dengan `review_mobil.csv`.
2. Periksa status kosong atau terisi mobil serta posisi poligon pada foto sumber.
3. Cocokkan tanggal dan pembagian dengan `manifest.json`, termasuk acuan kosong tiap petak.
4. Jika ada koreksi, catat foto, ID petak, label sebelumnya, label hasil pemeriksaan, nama pemeriksa, dan alasannya pada progres Minggu 13 sebelum evaluasi diperbarui.

Catatan kurasi yang tersedia dibuat melalui pemeriksaan visual asisten AI. Pemeriksaan ulang oleh anggota masih menjadi tugas minggu ini; jangan mengganti nama pemeriksa sebelum melakukan pemeriksaan sendiri.

Model memprediksi okupansi petak yang sudah ditentukan. Model belum dilatih membedakan mobil dari motor atau jenis objek lain.

## Sumber dan lisensi

Foto dalam data/images berasal dari PKLot, oleh Paulo R. L. de Almeida, Luiz S. Oliveira, Eunelson J. da Silva Jr., Alceu S. Britto Jr., dan Alessandro L. Koerich. Expert Systems with Applications 42(11), 4937–4949 (2015), doi:10.1016/j.eswa.2015.02.009.

Data digunakan berdasarkan CC BY 4.0, https://creativecommons.org/licenses/by/4.0/.
Distribusi foto dan anotasi diambil dari mirror Voxel51/PKLot, https://huggingface.co/datasets/Voxel51/PKLot.
Sumber resmi https://web.inf.ufpr.br/vri/databases/parking-lot-database/.

Perubahan dalam repositori ini mencakup pemilihan subset empat petak, konversi anotasi poligon ternormalisasi menjadi manifest JSON, kurasi visual asisten AI, dan pembuatan contact sheet. Foto pada data/images dipertahankan sesuai byte unduhan, dengan checksum SHA-256 di manifest.

[Pembagian tugas minggu ini](../progres/minggu13/README.md) · [Kembali ke halaman utama](../README.md)
