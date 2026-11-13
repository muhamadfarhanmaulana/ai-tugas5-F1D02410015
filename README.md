# ai-tugas5-F1D02410015

## Identitas
* **Nama:** Muahamad Farhan Maulana
* **NIM:** F1D02410015

## Topik dan Cara Menjalankan Program
* **Diagnosa Penyakit dan Hama Tanaman Melon**
* **Bahasa Pemrograman:** Python (versi 3.13)
* **Cara Menjalankan Program:**
  1. Pastikan file `main.py` dan `kb_melon.json` berada di dalam satu folder/direktori yang sama.
  2. Buka terminal atau Command Prompt pada direktori tersebut.
  3. Jalankan perintah berikut:
     ```bash
     python main.py
     ```
  4. Jawab pertanyaan bernomor dengan memasukkan huruf **`y`** (Ya) atau **`t`** (Tidak) sesuai kondisi gejala tanaman. 

## 3. Daftar Sumber Rujukan dan Tabel Aturan

### Daftar Sumber Literatur:
1. **Bambang Yuwono, dkk.** — *Sistem Pakar Berbasis Web untuk Diagnosa Hama dan Penyakit Pada Tanaman Melon*, Seminar Nasional Informatika UPN Yogyakarta, 2013.
2. **Zulkifli Arief** — *Rancang Bangun Aplikasi Mobile Untuk Mendiagnosis Penyakit pada Tanaman Melon Menggunakan Metode Certainty Factor*, Jurnal JATI (Jurnal Teknik Informatika) Vol. 2 No. 1, 2018.
3. **Dodi Prasetio** — *Respon Pertumbuhan dan Hasil Tanaman Melon Terhadap Pemberian Bokashi Kulit Nenas Dan Poc Daun Lamtoro*, Jurnal Ilmiah Mahasiswa Pertanian [JIMTANI] Vol. 2 No. 3, 2022.

### Tabel Aturan (*Knowledge Base*):
| ID Aturan | Premis / Syarat (Jika) | Konklusi / Hasil (Maka) | Sumber Rujukan |
| :--- | :--- | :--- | :--- |
| **R1** | Ada daun yang menggulung dalam 1 pohon, Pucuk tanaman kering | Gejala awal kutu daun | S2 (Zulkifli Arief) |
| **R2** | Gejala awal kutu daun, Terdapat getah cairan yang mengkilap pada akar | Kutu Daun Ringan | S2 (Zulkifli Arief) |
| **R3** | Daun menguning karena terendam air, Pertumbuhan tanaman terhambat | Stress Genangan dan Defisiensi Hara | S3 (Dodi Prasetio) |

## 4. Metode yang Dipilih
Metode yang digunakan pada sistem pakar ini adalah **Forward Chaining** (Pencairan Maju). 


* **Alasan Pemilihan:** *Forward Chaining* sangat cocok diterapkan karena proses diagnosis dimulai dari fakta awal berupa gejala-gejala yang diamati oleh pengguna (jawaban `y`/`t`), lalu dicocokkan dengan premis aturan dalam basis pengetahuan hingga menghasilkan kesimpulan akhir berupa identifikasi penyakit atau masalah tanaman.

## 5. Tiga Kasus Uji dan Tangkapan Layar (Screenshot)

### Kasus Uji 1 (Positif - Kutu Daun Ringan)
* **Gejala Masukan:** Daun menggulung dalam 1 pohon (`y`), pucuk tanaman kering (`y`), terdapat getah cairan mengkilap pada akar (`y`).
* **Hasil Eksekusi:** Berhasil melacak aturan `R1` dan `R2` hingga menghasilkan kesimpulan akhir **Kutu Daun Ringan**.
* **Screenshot:** *(Letakkan gambar tangkapan layar di folder `screenshot/kasus positif_1.png`)*

### Kasus Uji 2 (Positif - Stress Genangan dan Defisiensi Hara)
* **Gejala Masukan:** Daun menguning karena terendam air (`y`), pertumbuhan tanaman terhambat (`y`).
* **Hasil Eksekusi:** Berhasil melacak aturan `R3` hingga menghasilkan kesimpulan akhir **Stress Genangan dan Defisiensi Hara**.
* **Screenshot:** *(Letakkan gambar tangkapan layar di folder `screenshot/kasus positif_2.png`)*

### Kasus Uji 3 (Negatif - Tidak Ditemukan)
* **Gejala Masukan:** Semua gejala dijawab `t` (Tidak) atau tidak membentuk pola aturan yang valid.
* **Hasil Eksekusi:** Program berhenti pada siklus akhir dengan status kesimpulan **tidak ada (kasus negatif)**.
* **Screenshot:** *(Letakkan gambar tangkapan layar di folder `screenshot/kasus negatif.png`)*

## 6. Batas Keberlakuan
Basis pengetahuan sistem pakar ini disusun berdasarkan literatur jurnal ilmiah pertanian dan penelitian terkait hama serta penyakit tanaman melon dari Bambang Yuwono dkk., Zulkifli Arief, dan Dodi Prasetio. Sistem ini ditujukan untuk membantu diagnosis awal dan identifikasi gejala umum pada tanaman melon (*Cucumis melo L.*) dalam konteks pembelajaran serta edukasi pertanian. Hasil diagnosis dari program ini bersifat sebagai saran pendukung keputusan awal bagi petani dan bukan merupakan keputusan mutlak pengganti ahli agronomi atau pakar pertanian profesional.

## 7. Penggunaan Alat Bantu AI
* **Pernyataan:** Alat bantu yang saya gunakan dalam menegerjakan tugas ini gemini yang dimana sebagai bantua untuk mengetahui alur bagaimana cara kerjanya.