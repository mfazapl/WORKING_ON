# Langkah-langkah penilitian
1. Konversi dataset dari .flac menjadi .wav
2. Mengubah dataset yang sudah dikonversi menjadi bentuk gambar dalam bentuk diagram spectral
3. Pembuatan model
4. (bersambung)

# Library Yang dipakai
1. `ffmpeg`
2. `subproccess`
3. `librosa`
4. `keras`
5. `tensorflow`
6. `Os`

# Catatan
1. Pastikan dataset ASVspoof2019 sudah diunduh dan ektraksi
2. karena saya masih tahap konversi dan kebetulan belum selesai, saya ambil contoh pada `pa_dev_dataset`.

## 1. Konversi dataset dari .flac menjadi .wav
![folder](gambar/langkah1.PNG)

Siapkan folder baru untuk menyimpan hasil konversi seperti gambar atas.
______________________________________________________________________

![file_dev](gambar/langkah2.PNG)

buka folder `data_model`, lalu buka file `pa_dev_dataset`
_______________________________________________________________________
![input_dan_output_file](gambar/langkah3.PNG)

Pada bagian `input_file` dan `output_file`, ubah sesuai tempat penyimpanan masing-masing. `input_file` sebagai penyimpanan dataset `pa_dev_dataset` dan `output_file` sebagai tempat hasil konversi.

begitu terus hingga file la atau (Logis Attack).

## 2. Mengubah dataset yang sudah dikonversi menjadi bentuk gambar dalam bentuk diagram spectral
__________________________________________________________________________
![langkah2.1](gambar/langkah2.1.PNG)

Buat folder seperti gambar diatas. Untuk letak folder bebas ditaruh dimana.
_________________________________________________________________________
![langkah2.2](gambar/langkah2.2.PNG)

Didalam folder tersebut, buat folder baru seperti gambar diatas

*Penjelasan: 14 folder tersebut merupakan fitur ektraksi librosa, penilitian ini akan membandingkan semua fitur dan akan diliat akurasinya, lalu digunakan pada implementasi sistem.

![langkah2.3](gambar/langkah2.3.PNG)
![langkah2.4](gambar/langkah2.4.PNG)

![langkah2.5](gambar/langkah2.5.PNG)
![langkah2.6](gambar/langkah2.6.PNG)
![langkah2.7](gambar/langkah2.7.PNG)
![langkah2.8](gambar/langkah2.8.PNG)
![langkah2.9](gambar/langkah2.9.PNG)
![langkah2.10](gambar/langkah2.10.PNG)
![langkah2.11](gambar/langkah2.11.PNG)
![langkah2.12](gambar/langkah2.12.PNG)
![langkah2.13](gambar/langkah2.13.PNG)
![langkah2.14](gambar/langkah2.14.PNG)
![langkah2.15](gambar/langkah2.15.PNG)
![langkah2.16](gambar/langkah2.16.PNG)

Setiap folder fitur ektraksi terdapat enam folder tambahan guna menyimpan dataset. Seperti gambar diatas.
__________________________________________________________________________
