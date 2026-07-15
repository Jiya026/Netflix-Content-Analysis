import pandas as pd

#Importing the dataset
df = pd.read_csv(r"C:\Users\Admin\Desktop\Netflix_analysis\netflix_titles.csv")

#Basic functions
print("---------First 5 Rows--------")
print(df.head())

print("\n-------Size of the dataset------")
print(df.shape)

print("\n-----Names of all the columns------")
print(df.columns)

print("\n-----Info give summary of the dataset-----")
print(df.info())

print("\n-----null used to check null and sum used to do the sum of it--------")
print(df.isnull().sum())

print("\n----Duplicate rows sum-----")
print(df.duplicated().sum())

# # #remove duplicates
df = df.drop_duplicates()
print(df)

# #Data cleaning
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["listed_in"] = df["listed_in"].fillna("Unknown")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
print(df["date_added"].head())

#Feature engineering---> taking existing col n creating new
df["year_added"] = df["date_added"].dt.year #extract only year from the "date_added" col so new col created with year only
df["month_added"] = df["date_added"].dt.month_name() #extract only month from the "date_added" col so new col created with month only
df["content_age"] = df["year_added"] - df["release_year"]

#only df.month in no. month_name() in str---- line40

print(df)

# #Bussiness related questions
print("\n------Movies vs TV Shows--------")
print(df["type"].value_counts())

print("\n-----------ratings---------")
print(df["rating"].value_counts())

print("\n-----------More content is added asp year---------")
print(df["year_added"].value_counts().sort_index())

print("\n-----------More content is added asp month---------")
print(df["month_added"].value_counts().sort_index())

print("\n------Average released------")
print(df["release_year"].mean())

print("\n-------Top 10 countries entries-------")
print(df["country"].value_counts().head(10))

print("\n-----Rating distribution-------")
print(df["rating"].value_counts())

print("\n------Content age ie; when added ma n min---------")
print("\n Maximum Content Age:", df["content_age"].max())
print("\n Minimum Content Age:",df["content_age"].min())
print("\n Median Content Age:",df["content_age"].median())
print("\n Mode Content Age:",df["content_age"].mode())
print(df["content_age"].describe())

# #Visualization
import matplotlib.pyplot as plt

#Movies vs TV Shows (bar chart)
type_counts = df["type"].value_counts() #df["type"]---> take from whole dataset .value_counts ----> this will count movies+shows

plt.figure(figsize=(6,4)) #this will adjust the fig size not too small or large

type_counts.plot(
    kind="bar",
    color="green"
)

plt.gcf().set_facecolor("#f2f2f2") #chart background
plt.gca().set_facecolor("#ffffff") #plot area background
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()

# #Rating Distribution (bar chart)
type_ratings = df["rating"].value_counts().head(10)

plt.figure(figsize=(8,5))

type_ratings.plot(
    kind="bar",
    color="yellow"
)

plt.title("Top 10 Rating Distribution on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

#Titles Added per Year (line chart)
type_titles = df["year_added"].value_counts().sort_index() #.sort_index() Sorts years in ascending order.

plt.figure(figsize=(10,5))

type_titles.plot(kind="line", marker="o")
plt.title("Title Added per Year In Ascending order")
plt.xlabel("Title")
plt.ylabel("Count")
plt.show()

#Top 10 Countries Serving more on Netflix (horizontal bar chart)

type_top = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))

type_top.plot(kind="barh", color="red")
plt.title("Top 10 countries posting on netflix")
plt.xlabel("Count")
plt.ylabel("Countries")
plt.show()

#Content Released according per year
type_year = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))

type_year.plot(kind="line",color="red")   # use single color
plt.title("Netflix Content Released Per Year")
plt.xlabel("Year")
plt.ylabel("Density")
plt.grid(alpha=0.3)
plt.show()

import seaborn as sns

genre_counts = df["listed_in"].value_counts().head(10)

plt.figure(figsize=(8,4))

sns.barplot(
    x=genre_counts.values,
    y=genre_counts.index,
    color="red"
)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

#save cleaned dataset
df.to_csv(r"C:\Users\Admin\Desktop\Netflix_analysis\netflix_clean.csv", index=False)