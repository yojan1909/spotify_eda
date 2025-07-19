import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SpotifyFeatures.csv")  # or your Kaggle CSV file
print(df.shape)
print(df.columns)

# Drop duplicates or nulls if any
df.dropna(inplace=True)

# Correlation Matrix
plt.figure(figsize=(10, 8))
corr = df[['popularity', 'tempo', 'energy', 'valence', 'loudness', 'danceability']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

#  Average Popularity by Genre
genre_pop = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)
fig = px.bar(genre_pop, title="Top 10 Genres by Average Popularity")
fig.show()

#  Tempo vs Popularity
fig = px.scatter(df, x='tempo', y='popularity', color='genre', title="Tempo vs Popularity")
fig.show()

#  Energy vs Popularity
fig = px.scatter(df, x='energy', y='popularity', color='genre', title="Energy vs Popularity")
fig.show()

#  Histogram of Tempo and Energy
fig = px.histogram(df, x='tempo', nbins=50, title="Tempo Distribution")
fig.show()

fig = px.histogram(df, x='energy', nbins=50, title="Energy Distribution")
fig.show()

# Songs by Year
if 'year' in df.columns:
    year_trend = df.groupby('year').size()
    fig = px.line(year_trend, title="Songs Released Per Year")
    fig.show()
