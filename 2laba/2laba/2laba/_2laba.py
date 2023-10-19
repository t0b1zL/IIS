import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/netflix_titles.csv')

print(data.head())

print("Kilkist ryadkiv i stovptsiv:", data.shape)

print("Nazvy stovptsiv:", data.columns)

print("Typy danykh:", data.dtypes)

print("Kilkist unikalnykh znachen:")
print(data.nunique())

print("Kilkist propushchenykh znachen:")
print(data.isnull().sum())

movies_2019 = data[data["release_year"] == 2019]
genre_counts = movies_2019["listed_in"].str.split(", ").explode().value_counts()
print("Zhanr z naybilshoyu kilkistyu proektiv u 2019 rotsi:", genre_counts.index[0])

top_countries = data["country"].str.split(", ").explode().value_counts().head(10)

plt.figure(figsize=(12, 6))
top_countries.plot(kind="area")
plt.title("TOP-10 krayin za kilka proektiv na Netflix")
plt.xlabel("Country")
plt.ylabel("Kilkist proektiv")
plt.xticks(rotation=45)
plt.show()

old_movies = data[data["release_year"] < 1960]
country_with_most_old_movies = old_movies["country"].str.split(", ").explode().mode()[0]
print("Krayina, yaka vypustyla naybilshe starykh filmiv na Netflix:", country_with_most_old_movies)

data["month"] = pd.to_datetime(data["date_added"], format='%B %d, %Y', errors='coerce').dt.month

spring_movies = data[(data["month"] >= 3) & (data["month"] <= 5) & (data["type"] == "Movie")]
fall_movies = data[(data["month"] >= 9) & (data["month"] <= 11) & (data["type"] == "Movie")]
spring_series = data[(data["month"] >= 3) & (data["month"] <= 5) & (data["type"] == "TV Show")]
fall_series = data[(data["month"] >= 9) & (data["month"] <= 11) & (data["type"] == "TV Show")]

print("Vykhodyat filmy na Netflix:")
print("Vesnoyu:", len(spring_movies))
print("Osinnyu:", len(fall_movies))
print("Vykhodyat serialy na Netflix:")
print("Vesnoyu:", len(spring_series))
print("Osinnyu:", len(fall_series))

movie_counts_by_year = data[data["type"] == "Movie"]["release_year"].value_counts()
year_with_most_movies = movie_counts_by_year.idxmax()
print("Rik, u yakomu na Netflix vypushcheno naybilshe filmiv:", year_with_most_movies)