# Pertemuan 10 - String dan Pengolahan Teks
Nama: Azkiah Safira  
NIM: 2225250013  
Kelas: 3F

## Tujuan
Mengolah dan menormalisasi data teks menggunakan string Python. Melalui latihan dan praktik ini, mahasiswa mempelajari cara menyimpan teks dalam variabel, menghitung panjang teks, mengakses karakter menggunakan indeks positif dan negatif, serta mengambil bagian teks menggunakan slicing.
Mahasiswa juga mempelajari penggunaan berbagai method string, seperti `upper()`, `lower()`, `title()`, `strip()`, `replace()`, `split()`, dan `find()` untuk mengubah format teks, membersihkan spasi, mengganti bagian teks, memisahkan kata, serta mencari posisi kata dalam sebuah kalimat.
Selain itu, mahasiswa mempelajari cara membersihkan dan menormalisasi teks agar data memiliki format yang lebih konsisten. Materi ini diterapkan dalam praktik normalisasi data mahasiswa, meliputi pembersihan spasi, penyeragaman format nama dan kelas, serta pengolahan data teks agar lebih mudah dibaca dan digunakan.

## Struktur Program
Program Pertemuan 10 terdiri atas enam file latihan dan satu file tugas yang disusun berdasarkan materi string dan pengolahan teks.
Folder `latihan` berisi enam file Python sebagai berikut:
1. `01_dasar_string.py` — mempelajari pembuatan variabel string, penyimpanan teks, dan penggunaan fungsi `len()` untuk menghitung panjang teks.
2. `02_indeks_dan_slicing.py` — mempelajari akses karakter menggunakan indeks positif dan negatif serta pengambilan bagian teks menggunakan slicing.
3. `03_method_string.py` — mempelajari penggunaan method string, seperti `upper()`, `lower()`, `title()`, dan `replace()` untuk mengubah format teks.
4. `04_pembersihan_teks.py` — mempelajari cara membersihkan spasi di awal dan akhir teks menggunakan method `strip()`.
5. `05_normalisasi_teks.py` — mempelajari normalisasi teks dengan menghapus spasi berlebih dan menyeragamkan format penulisan.
6. `06_pencarian_kata.py` — mempelajari pencarian kata dalam teks menggunakan operator `in` dan method `find()`.

Folder `tugas` berisi file `normalisasi_data_mahasiswa.py`. Program ini mengolah data nama, NIM, dan kelas mahasiswa dengan membersihkan spasi yang tidak diperlukan, menyeragamkan format penulisan nama, serta mengubah format kelas menjadi huruf kapital. Hasil pengolahan ditampilkan dalam bentuk data mahasiswa yang lebih rapi dan konsisten.

Folder `dokumen` berisi file kuis formatif Pertemuan 10 yang digunakan untuk menguji pemahaman mengenai string dan pengolahan teks.

File `.gitignore` digunakan untuk mengecualikan file sementara, cache Python, dan file konfigurasi tertentu yang tidak perlu dimasukkan ke repositori Git.

## Cara Menjalankan
Jalankan terminal pada folder proyek Pertemuan 10. Pastikan Python telah terpasang, kemudian jalankan program tugas menggunakan perintah berikut:

    python3 tugas/normalisasi_data_mahasiswa.py

Jika menggunakan Windows, program juga dapat dijalankan menggunakan perintah:

    python tugas/normalisasi_data_mahasiswa.py

Untuk menjalankan file latihan, gunakan perintah sesuai nama file yang ingin dijalankan. Contohnya:

    python3 latihan/01_dasar_string.py

Contoh menjalankan latihan normalisasi teks:

    python3 latihan/05_normalisasi_teks.py
Pastikan nama folder dan file sesuai dengan struktur program agar setiap program dapat dijalankan dengan benar.

## Algoritma
Program normalisasi data mahasiswa dilakukan melalui beberapa tahapan berikut:
1. Menyiapkan data nama, NIM, dan kelas mahasiswa dalam bentuk string.
2. Membersihkan spasi yang tidak diperlukan pada awal dan akhir teks menggunakan `strip()`.
3. Menghapus spasi berlebih di antara kata pada nama menggunakan kombinasi `split()` dan `join()`.
4. Menyeragamkan format nama menggunakan `title()` dan format kelas menggunakan `upper()`.
5. Menyimpan hasil normalisasi ke dalam struktur data dictionary.
6. Menampilkan nama, NIM, dan kelas mahasiswa yang telah dinormalisasi.

## Test Case
Pengujian dilakukan untuk memastikan program dapat mengakses karakter, mengambil bagian teks, menggunakan method string, membersihkan spasi, mencari kata, dan menormalisasi data mahasiswa.
| No. | Data/Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `"Matematika"` | Panjang teks = 10 | Diisi setelah pengujian | Diisi setelah pengujian |
| 2 | `"Algoritma"` dengan slicing `[0:4]` | `"Algo"` | Diisi setelah pengujian | Diisi setelah pengujian |
| 3 | `"  Azkiah Safira  "` dengan `strip()` | `"Azkiah Safira"` | Diisi setelah pengujian | Diisi setelah pengujian |
| 4 | `"  azkiah   safira  "` dengan normalisasi nama | `"Azkiah Safira"` | Diisi setelah pengujian | Diisi setelah pengujian |
| 5 | `"  azkiah   safira  "`, NIM `" 2225250013 "`, kelas `" 3f "` | Nama = `"Azkiah Safira"`, NIM = `"2225250013"`, kelas = `"3F"` | Diisi setelah pengujian | Diisi setelah pengujian |

Hasil aktual dan status diisi berdasarkan hasil program yang benar-benar dijalankan. Pengujian dinyatakan berhasil apabila hasil aktual sesuai dengan hasil yang diharapkan.

## Refleksi
Saya memahami bahwa string digunakan untuk menyimpan dan mengolah data berbentuk teks. Indeks digunakan untuk mengakses karakter tertentu, sedangkan slicing digunakan untuk mengambil bagian dari teks. Berbagai method string juga membantu mengubah format penulisan, membersihkan spasi, mengganti kata, dan mencari bagian teks tertentu.

Saya juga memahami bahwa normalisasi teks diperlukan agar data memiliki format yang konsisten dan lebih mudah diolah. Salah satu masalah yang dapat terjadi adalah adanya spasi berlebih pada nama atau data mahasiswa. Masalah tersebut dapat diatasi menggunakan `strip()`, `split()`, dan `join()` sebelum data ditampilkan atau diproses lebih lanjut.