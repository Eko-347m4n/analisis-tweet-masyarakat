import pandas as pd
from datetime import timedelta

file_path = "cleaned_data.csv"

df = pd.read_csv(file_path)

# Konversi kolom 'created_at' ke datetime
df['created_at'] = pd.to_datetime(df['created_at'], format='%I:%M %p %b %d, %Y')

# Tambahkan 7 jam ke kolom 'created_at'
df['created_at'] = df['created_at'] + timedelta(hours=7)

# Format kolom 'created_at' kembali ke format yang diinginkan
df['created_at'] = df['created_at'].dt.strftime('%I:%M %p %b %d, %Y')

# Simpan data yang sudah diperbarui ke file yang sama
df.to_csv(file_path, index=False)

print(f"7 jam telah ditambahkan ke kolom created_at di {file_path}")