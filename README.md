# Proyek Penambangan Data dan Visualisasi

Repositori ini berisi skrip dan data yang berkaitan dengan proyek penambangan dan analisis data.

## Ikhtisar Berkas

- `crawling.py`

  - Skrip ini ditujukan untuk akuisisi data, kemungkinan digunakan untuk menambang data dari suatu sumber (misalnya, Twitter) berdasarkan kata kunci atau kriteria tertentu. Fungsionalitas pastinya untuk pengambilan data tidak dijelaskan secara rinci dalam konteks saat ini, tetapi berfungsi sebagai komponen utama pengumpulan data.

- `generasi_emas_2045.csv`

  - Berkas CSV ini berisi data mentah yang berkaitan dengan "generasi emas 2045" sebelum dibersihkan atau diproses. Ini adalah salah satu dataset utama untuk proyek ini.

- `processing.py`

  - Skrip Python ini bertanggung jawab untuk pembersihan dan transformasi data. Ini melakukan operasi seperti:
    - Menambahkan header yang sesuai ke `generasi_emas_2045.csv` (berdasarkan `polri.csv`).
    - Memilih kolom tertentu (`created_at`, `full_text`, `tweet_url`).
    - Memformat stempel waktu `created_at`.
    - Menyesuaikan stempel waktu `created_at` dengan menambahkan 7 jam.
    - Menyimpan data yang diproses ke dalam berkas CSV baru (`cleaned_data.csv`).

- `cleaned_data.csv`

  - Berkas CSV ini adalah keluaran dari `processing.py`. Ini berisi data yang telah dibersihkan dan ditransformasi dari `generasi_emas_2045.csv`, dengan kolom yang dipilih dan stempel waktu yang disesuaikan, siap untuk visualisasi atau analisis lebih lanjut.

- `visualisasi.py`

  - Skrip Python ini digunakan untuk visualisasi data. Ini membaca data dari `cleaned_data.csv` dan menghasilkan plot (misalnya, frekuensi tweet dari waktu ke waktu) untuk memberikan wawasan tentang dataset. Ini menggunakan pustaka seperti pandas, matplotlib, dan seaborn untuk manipulasi dan plotting data.

## Analisis Statistik Deskriptif `cleaned_data.csv`

Berikut adalah analisis singkat dari statistik deskriptif dataset `cleaned_data.csv` yang dihasilkan setelah proses pembersihan:

1. **Kolom `created_at`**

   - `count`: 10606 → Total data (tweet) yang dianalisis adalah 10.606.
   - `unique`: 5854 → Hanya ada 5.854 nilai waktu yang berbeda. Ini menunjukkan bahwa banyak tweet dibuat pada waktu yang sama (kemungkinan retweet/quote tweet/spam bot).
   - `top`: "10:05 AM Jul 08, 2025" → Waktu paling sering muncul.
   - `freq`: 28 → Terdapat 28 tweet yang diposting pada waktu tersebut.

2. **Kolom `full_text`**

   - `unique`: 6605 → Dari 10.606 tweet, hanya 6.605 yang memiliki teks unik. Sisanya (4.001) merupakan duplikasi (bisa jadi retweet, spam, copy-paste).
   - `top`: " @sskusuzy Peran masyarakat sangat penting dala..." → Ini adalah teks yang paling sering muncul.
   - `freq`: 20 → Teks ini muncul sebanyak 20 kali.

3. **Kolom `tweet_url`**

   - `unique`: 6895 → Ada 6.895 tautan tweet yang unik, artinya sekitar 3.711 tweet memiliki URL yang sama (bisa jadi hasil embed, retweet tanpa kutipan, atau data error).
   - `top`: "https://x.com/undefined/status/194181896113977..." → URL yang paling sering muncul, kemungkinan besar ini adalah hasil scraping yang gagal (undefined).
   - `freq`: 3 → Muncul sebanyak 3 kali.
