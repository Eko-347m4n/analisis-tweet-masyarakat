import pandas as pd
import matplotlib
matplotlib.use('Agg') # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# Load the dataset
df = pd.read_csv('cleaned_data.csv')

# --- Basic Info (can be commented out for cleaner final output) ---
# print("Dataset Info:")
# df.info()
# print("\nFirst 5 rows of the dataset:")
# print(df.head())
# print("\nDescriptive Statistics:")
# print(df.describe())
# ---------------------------------------------------------------------

# Convert 'created_at' to datetime objects
df['created_at'] = pd.to_datetime(df['created_at'], format='%a %b %d %H:%M:%S %z %Y')

# --- Text Preprocessing Function ---
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text) # Remove URLs
    text = re.sub(r'@\w+', '', text)    # Remove mentions
    text = re.sub(r'#\w+', '', text)    # Remove hashtags
    text = text.lower()                   # Convert to lowercase
    words = re.findall(r'\b\w+\b', text) # Tokenize
    return words

# --- Sentiment Analysis ---

# Simple Indonesian sentiment lexicon
positive_words = set(['dukung', 'semangat', 'bangga', 'hebat', 'maju', 'sukses', 'terbaik', 'optimis', 'kreatif', 'inovatif', 'sehat', 'cerdas', 'kuat', 'peduli', 'harapan', 'solusi', 'positif', 'apresiasi', 'selamat', 'terima', 'kasih', 'bagus', 'baik', 'unggul', 'mandiri', 'sejahtera', 'aman', 'damai', 'bersama', 'gotong', 'royong', 'sinergi', 'kolaborasi', 'penting', 'nyata', 'wujudkan', 'membangun', 'meningkatkan', 'memperkuat', 'melindungi', 'menjaga', 'mendukung'])
negative_words = set(['tidak', 'bukan', 'gagal', 'masalah', 'korupsi', 'hancur', 'rusak', 'buruk', 'negatif', 'khawatir', 'ancaman', 'bahaya', 'krisis', 'sulit', 'miskin', 'sakit', 'lemah', 'bodoh', 'stunting', 'korban', 'melanggar', 'melawan', 'menolak', 'menghambat', 'mengancam', 'merusak', 'menghancurkan', 'bohong', 'palsu', 'curang', 'jahat', 'kejam', 'marah', 'benci', 'kecewa', 'sedih', 'takut', 'cemas', 'ragu', 'pesimis', 'salah', 'keliru', 'kurang'])

def get_sentiment(text):
    words = preprocess_text(text)
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['full_text'].apply(get_sentiment)

# Create and save the sentiment pie chart
plt.figure(figsize=(8, 8))
sentiment_counts = df['sentiment'].value_counts()
sns.set_palette(['#66c2a5','#fc8d62','#8da0cb']) # Colorblind-friendly palette
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})
plt.title('Sentiment Analysis of Tweets', fontsize=16)
plt.ylabel('') # Hide the y-label
plt.savefig('sentiment_analysis.png')
print("Plot analisis sentimen telah disimpan sebagai sentiment_analysis.png")

# --- Bigram Frequency Analysis (Existing Code) ---

# Combine all text into one string
text_full = ' '.join(df['full_text'].dropna())
words_full = preprocess_text(text_full)

# Simple list of Indonesian stop words to exclude
stop_words = set([
    'di', 'dan', 'yang', 'ke', 'dari', 'ini', 'itu', 'dengan', 'untuk', 'pada', 'sebagai', 'akan',
    'adalah', 'dalam', 'tidak', 'bukan', 'juga', 'telah', 'oleh', 'kita', 'mereka', 'saya', 'kami',
    'anda', 'bisa', 'jadi', 'karena', 'tapi', 'sudah', 'belum', 'sangat', 'agar', 'atau', 'saat',
    'yg', 'gak', 'ga', 'ke', 'aja', 'kok', 'sih', 'ya', 'aja', 'deh', 'nya', 'kok', 'dah', 'aja',
    'buat', 'biar', 'banget', 'nan'
])

# Filter out stop words and numbers
filtered_words = [word for word in words_full if word not in stop_words and not word.isdigit()]

# Generate bigrams
bigrams = zip(filtered_words, filtered_words[1:])
bigram_counts = Counter(bigrams)
most_common_bigrams = bigram_counts.most_common(20)

# Create a DataFrame for plotting
df_bigram_freq = pd.DataFrame(most_common_bigrams, columns=['Bigram', 'Frequency'])
df_bigram_freq['Bigram'] = df_bigram_freq['Bigram'].apply(lambda x: ' '.join(x))

# Create and Save the Bigram Plot
plt.figure(figsize=(12, 10))
sns.barplot(x='Frequency', y='Bigram', data=df_bigram_freq, hue='Bigram', palette='viridis', legend=False)
plt.title('Top 20 Most Frequent Two-Word Phrases (Bigrams)')
plt.xlabel('Frequency')
plt.ylabel('Two-Word Phrase')
plt.tight_layout()
plt.savefig('bigram_frequency.png')
print("Plot frekuensi bigram telah disimpan sebagai bigram_frequency.png")
