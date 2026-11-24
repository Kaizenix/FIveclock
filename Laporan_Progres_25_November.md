# Evaluasi Fiveclock per 25 November 2026

Eksperimen menggunakan foto PKLot UFPR04 asli. Paket berisi implementasi enam skenario, anotasi terpilih, hasil prediksi, model SVM, dan bukti visual.

## Data dan protokol

Sebanyak 64 foto diambil melalui mirror Voxel51/PKLot. Foto tetap berasal dari PKLot. Anotasi koordinat dan okupansi pada mirror berformat FiftyOne, kemudian dikonversi menjadi manifest JSON. Versi mirror dicatat pada data/source.json dan checksum tiap citra disimpan dalam manifest.

- Empat petak dipilih, ID 1, 2, 3, dan 4.
- Kalibrasi memakai empat foto berbeda dari 7 Desember 2012, masing-masing sebagai acuan kosong satu petak.
- Pengembangan memakai 24 foto dari 8, 11, dan 12 Desember 2012, delapan foto per tanggal. Ada 96 observasi, terdiri atas 28 kosong dan 68 mobil.
- Pengujian memakai 36 foto dari 14, 15, dan 16 Desember 2012, dua belas foto per tanggal. Ada 144 observasi, terdiri atas 56 kosong dan 88 mobil.
- Pemilihan foto dilakukan dengan interval indeks merata setelah diurutkan menurut waktu, sebelum mengukur kinerja. ID petak ditetapkan sebelum evaluasi.
- Tanggal kalibrasi, pengembangan, dan uji saling terpisah.
- Pemeriksaan visual dilakukan oleh asisten AI pada 256 crop petak dalam contact_0.jpg sampai contact_7.jpg, mencakup keempat petak pada semua foto. Pada area yang dinilai terlihat mobil atau petak kosong sesuai label. Beberapa objek lain terlihat di sekitar petak. Kategori kendaraan tidak diprediksi oleh model.
- Foto uji memuat 22 foto berawan, 11 cerah, dan 3 hujan. Jumlah sampel tiap kondisi berbeda.

## Metode

Baseline memakai selisih grayscale terhadap acuan, lalu thresholding dan rasio piksel aktif dalam poligon. Metode klasik lengkap menambahkan normalisasi P5–P95 pada area gabungan empat petak, Canny 50/150, OR, serta opening dan closing kernel 3×3. Area kerja berukuran 960×540. Tepi acuan diberi toleransi satu piksel sebelum tepi baru didilasi.

Ambang selisih {15,25,35} dan okupansi {0,10;0,20;0,30} dipilih pada data pengembangan. Baseline dan metode lengkap sama-sama memilih 35 dan 0,30. Ketiga ablasi memakai parameter metode lengkap. SVM linear memakai HOG OpenCV, citra petak 64×64, standardisasi fitur dari data pengembangan, C=1, dan class_weight=balanced. Model SVM tetap menerima grayscale tanpa normalisasi P5–P95.

Parameter ditetapkan sebelum pengujian. Label uji dipakai dalam penghitungan metrik. Data uji yang sama digunakan untuk keenam skenario.

## Hasil pengujian

| Skenario | Macro-F1 | Akurasi | Kosong terbaca mobil | Mobil terbaca kosong |
|---|---:|---:|---:|---:|
| baseline | 0.8579 | 87.50% | 18 | 0 |
| klasik_lengkap | 0.4696 | 64.58% | 51 | 0 |
| tanpa_normalisasi | 0.7941 | 82.64% | 25 | 0 |
| tanpa_canny | 0.6898 | 75.69% | 35 | 0 |
| tanpa_morfologi | 0.4696 | 64.58% | 51 | 0 |
| hog_svm | 0.9569 | 95.83% | 0 | 6 |

HOG + SVM mencapai macro-F1 0,9569 dan akurasi 95,83%, dengan 138 dari 144 prediksi benar. Selisih macro-F1 terhadap baseline adalah +0,0991. Semua 56 petak kosong diprediksi benar. Enam dari 88 petak terisi mobil diprediksi kosong.

Metode klasik lengkap mencapai macro-F1 0,4696. Sebanyak 51 dari 56 petak kosong diprediksi terisi. Target proposal macro-F1 ≥ 0,85 untuk metode klasik lengkap belum tercapai.

## Hasil ablasi

- Menghilangkan normalisasi meningkatkan macro-F1 sebesar 0,3245 terhadap metode lengkap dan mengurangi petak kosong yang salah terbaca mobil dari 51 menjadi 25. Dalam konfigurasi ini, normalisasi berdasarkan persentil pada area yang juga berisi mobil sensitif terhadap komposisi intensitas. Temuan ini merupakan alasan mengembangkan strategi normalisasi lain menggunakan data pengembangan baru.
- Menghilangkan Canny meningkatkan macro-F1 sebesar 0,2202 dan mengurangi kesalahan kosong terbaca mobil menjadi 35. Penggabungan OR dapat menambah perubahan dari tepi bayangan dan tekstur. Ablasi menunjukkan jalur tepi tambahan belum membantu pada konfigurasi yang diuji.
- Menghilangkan morfologi menghasilkan skor dan status prediksi yang sama dengan metode lengkap. Ini menunjukkan perubahan mask belum cukup mengubah keputusan terhadap ambang okupansi pada sampel uji tersebut.

## Kasus gagal dan keterbatasan

Enam salah prediksi SVM terdapat pada foto berawan. Crop kasus gagal tersedia pada results/kasus_gagal_svm.png. Citra mencakup kondisi redup atau kabur serta perubahan penampilan mobil. Penyebab tiap kesalahan memerlukan pengujian lanjutan, sehingga atribut tersebut diperlakukan sebagai observasi visual.

Evaluasi memakai empat petak dari satu kamera dan hanya tiga tanggal uji. Foto yang berbeda tetap dapat memuat mobil yang sama. Hasil menggambarkan perpindahan tanggal pada petak yang sudah dikenal. Pengujian pada petak dan kamera baru memerlukan pembagian data tambahan. Skor per cuaca bersifat deskriptif, terutama kategori hujan yang hanya terdiri atas 12 observasi petak.

## Status pekerjaan per 25 November

Implementasi, pelatihan SVM, baseline, tiga ablasi, evaluasi 144 observasi data asli, ekspor CSV, dan visualisasi telah dijalankan. Pemeriksaan jenis kendaraan dalam paket merupakan pemeriksaan asisten AI. Tim dapat memeriksanya kembali melalui contact sheet yang disertakan.

Kode dan hasil evaluasi sudah tersedia di repositori kelompok. Pembagian pekerjaan lanjutan tiap anggota dicatat pada [progres Minggu 13](progres/minggu13/README.md). Aplikasi demo akhir, laporan akhir, slide, dan video termasuk pekerjaan tahap berikutnya. Pemenuhan target metode klasik lengkap masih memerlukan pengembangan. Jika metode diperbaiki, evaluasi berikutnya memerlukan pemisahan pengujian baru atau pelabelan jelas sebagai iterasi setelah melihat hasil uji.

## Sumber

- Dataset resmi PKLot https://web.inf.ufpr.br/vri/databases/parking-lot-database/
- Mirror dengan foto dan anotasi poligon https://huggingface.co/datasets/Voxel51/PKLot
- de Almeida dkk. (2015), PKLot – A robust dataset for parking lot classification, doi:10.1016/j.eswa.2015.02.009.
- Lisensi data CC BY 4.0 https://creativecommons.org/licenses/by/4.0/
