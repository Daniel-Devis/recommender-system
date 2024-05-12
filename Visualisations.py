import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import ast
import numpy as np


# Load your dataset
df = pd.read_csv('ml-25m/movies4.csv')

df = df[~df['genres'].apply(ast.literal_eval).apply(lambda x: '(no genres listed)' in x)]

# Preprocess genres: Convert from string representation of list to actual list and explode
df['genres'] = df['genres'].apply(ast.literal_eval)
genres_exploded = df.explode('genres')


# Generate Genre Popularity visualization
genre_counts = genres_exploded['genres'].value_counts()
plt.figure(figsize=(12, 8))
genre_counts.plot(kind='bar', color='cadetblue')
plt.title('Popularity of Genres')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Generate Movie Releases Over Years visualization
movies_per_year = df.groupby('year').size()
plt.figure(figsize=(12, 8))
movies_per_year.plot(kind='line', color='tomato', marker='o')
plt.title('Number of Movies Released Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.show()



# Bubble Chart for Genres
genre_year_counts = genres_exploded.groupby(['year', 'genres']).size().unstack(fill_value=0)
years = genre_year_counts.index
genres = genre_year_counts.columns
sizes = genre_year_counts.values

plt.figure(figsize=(15, 10))
for i, genre in enumerate(genres):
    plt.scatter(years, np.full(len(years), i), s=sizes[:, i]*10, alpha=0.5, label=genre)
plt.yticks(ticks=np.arange(len(genres)), labels=genres)
plt.title('Popularity of Genres Over Years (Bubble Size Reflects Frequency)')
plt.xlabel('Year')
plt.ylabel('Genres')
plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

# Stacked Bar Chart for Genres by Year
plt.figure(figsize=(15, 10))
bottom_values = np.zeros(len(years))
for genre in genres:
    plt.bar(years, genre_year_counts[genre], bottom=bottom_values, label=genre)
    bottom_values += genre_year_counts[genre].values
plt.title('Distribution of Movie Counts Per Genre Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()

# LINE GRAPH instead of STACKED BAR CHART
plt.figure(figsize=(15, 10))
for genre in genres:
    plt.plot(years, genre_year_counts[genre], label=genre, marker='o')
plt.title('Distribution of Movie Counts Per Genre Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()