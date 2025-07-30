import pandas as pd

# Baca data mentah dari kedua file
df1 = pd.read_csv('generasi_emas_2045.csv')
df2 = pd.read_csv('generasi_emas1_2045.csv')

# Gabungkan kedua dataframe
df = pd.concat([df1, df2], ignore_index=True)

# Pilih kolom yang diinginkan
df_cleaned = df[['created_at', 'full_text', 'tweet_url']]

# Simpan ke file baru
df_cleaned.to_csv('cleaned_data.csv', index=False)

print("cleaned_data.csv berhasil dibuat dengan kolom yang dipilih dari kedua file sumber.")
