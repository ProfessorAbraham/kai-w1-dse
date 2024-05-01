import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
df = pd.read_csv('C:\\Users\\Professor Ab\\OneDrive - amu.edu.et\\Desktop\\Data Science\\kai-w1-dse\\data\\raw_analyst_ratings.csv')

# Task 1: Descriptive Statistics for Textual Lengths (Headline Length)
# Calculate the length of headlines
df['headline_length'] = df['headline'].apply(len)

# Obtain descriptive statistics for headline lengths
headline_length_stats = df['headline_length'].describe()
print("Descriptive Statistics for Headline Lengths:")
print(headline_length_stats)

# Task 2: Number of Articles per Publisher
# Count the number of articles per publisher
publisher_counts = df['publisher'].value_counts()

# Display the count of articles per publisher
print("\nNumber of Articles per Publisher:")
print(publisher_counts)

# Task 3: Publication Dates Analysis
# Convert 'date' column to datetime with 'coerce' option to handle errors
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing or incorrect dates
df = df.dropna(subset=['date'])

# Extract day of the week
df['day_of_week'] = df['date'].dt.day_name()

# Count the number of articles published on each day of the week
publication_day_counts = df['day_of_week'].value_counts()

# Plot the publication frequency over days of the week
plt.figure(figsize=(10, 6))
publication_day_counts.plot(kind='bar', color='skyblue')
plt.title('Publication Frequency by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
