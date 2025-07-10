import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('cleaned_data.csv')

# Display basic information about the dataset
print("Dataset Info:")
df.info()

# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Convert 'created_at' to datetime objects
df['created_at'] = pd.to_datetime(df['created_at'], format='%I:%M %p %b %d, %Y')

# Extract date for daily tweet count
df['date'] = df['created_at'].dt.date

# Visualize the number of tweets per day
# plt.figure(figsize=(15, 7))
# sns.countplot(x='date', data=df, palette='viridis')
# plt.title('Number of Tweets per Day')
# plt.xlabel('Date')
# plt.ylabel('Number of Tweets')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# You can add more visualizations here based on 'full_text' if needed,
# for example, word frequency or sentiment analysis, but that would require
# more complex text processing.

