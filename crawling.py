import time
import pandas as pd
import os
from datetime import datetime
import subprocess

# Konfigurasi awal
twitter_auth_token = 'change with your cookie'
filename = 'generasi_emas_2045.csv'
limit_per_keyword = 111
wait_seconds = 60  # 10 menit
temp_folder = 'tweets-data'

# Kata kunci dan hashtag
keywords = [
    '"anak generasi emas"',
    '"generasi emas 2045"',
    '"generasi masa depan"',
    '"anak indonesia 2045"',
    '"tunas bangsa"',
    '"pembangunan generasi"',
    '"penerus bangsa"',
    '"kolaborasi bangsa"',
    '"kerja sama demi anak"',
    '"mewujudkan indonesia emas"',
    '"peran masyarakat"',
    '"peran keluarga"',
    '"tanggung jawab bersama"',
    '"investasi SDM"',
    '#GenerasiEmas2045',
    '#AnakGenerasiEmas',
    '#AnakIndonesia',
    '#Indonesia2045',
    '#HariAnak',
    '#HAN2025',
    '#IndonesiaEmas',
    '#BersamaAnak',
    '#Kolaborasi2045',
    '#SDMUnggul',
    '#IndonesiaMaju',
    '#TanggungJawabBersama'
]

# Buat folder jika belum ada
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

# Buat file utama jika belum ada
if not os.path.exists(filename):
    pd.DataFrame(columns=["id_str"]).to_csv(filename, index=False)

# Load id_str yang sudah ada
existing_df = pd.read_csv(filename)
existing_ids = set(existing_df['id_str'].astype(str).tolist())

# Mulai crawling per keyword
for i, keyword in enumerate(keywords):
    print(f"\n📥 Memulai crawling untuk keyword: '{keyword}' ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

    temp_filename = f"temp_{i}.csv"
    temp_path = os.path.join(temp_folder, temp_filename)
    query_string = f"{keyword} lang:id"

    try:
        command = [
            'npx', '-y', 'tweet-harvest@latest',
            '-o', temp_filename,
            '-s', query_string,
            '--tab', 'LATEST',
            '-l', str(limit_per_keyword),
            '--token', twitter_auth_token
        ]

        # Pindahkan file sementara ke folder temp
        command.insert(4, os.path.join(temp_folder, temp_filename))

        result = subprocess.run(command, capture_output=True, text=True)

        print("=== STDOUT ===")
        print(result.stdout)
        print("=== STDERR ===")
        print(result.stderr)

        if os.path.exists(temp_path):
            df_temp = pd.read_csv(temp_path)

            if 'id_str' not in df_temp.columns:
                print("❌ Kolom 'id_str' tidak ditemukan pada hasil scraping.")
                continue

            df_temp['id_str'] = df_temp['id_str'].astype(str)

            # Filter tweet yang belum ada
            df_new = df_temp[~df_temp['id_str'].isin(existing_ids)]

            if not df_new.empty:
                df_new.to_csv(filename, mode='a', header=False, index=False)
                existing_ids.update(df_new['id_str'].tolist())
                print(f"✅ {len(df_new)} tweet baru ditambahkan untuk keyword '{keyword}'.")

            else:
                print(f"⚠️ Tidak ada tweet baru untuk keyword '{keyword}'.")

            os.remove(temp_path)
        else:
            print(f"❌ File sementara tidak ditemukan untuk keyword '{keyword}'. Kemungkinan scraping gagal.")

    except Exception as e:
        print(f"❌ Gagal menjalankan tweet-harvest untuk keyword '{keyword}':", e)

    if i < len(keywords) - 1:
        print(f"🕒 Menunggu {wait_seconds} detik sebelum keyword berikutnya...")
        time.sleep(wait_seconds)

print("\n🏁 Proses crawling selesai.")
