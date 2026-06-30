import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("clean_books.csv")

print(df.head())
# to view information about the dataset
print(df.info())
# to view the summary statistics of the dataset
print(df.describe())
# to view datatypes of each column
print(df.dtypes)    
# checking for missing values
print(df.isnull().sum())    
# checking for duplicates
print(df.duplicated().sum())
# Average book price
print("Average Price:", df["Price"].mean())
# maximum book price
print("Maximum Price:", df["Price"].max())
# minimum book price
print("Minimum Price:", df["Price"].min())  
# count books by rating
print("Books by Rating:")
print(df["Rating"].value_counts())
# visualizing the distribution of book ratings
sns.countplot(x="Rating", data=df)

plt.title("Book Ratings")

plt.show()
# visulaization of the distribution of book prices
plt.figure(figsize=(8,5))

sns.histplot(df["Price"], bins=20)

plt.title("Price Distribution")

plt.show()
# box plot to visualize the distribution of book prices
plt.figure(figsize=(8,5))

sns.boxplot(x=df["Price"])

plt.title("Price Boxplot")

plt.show()
# rating vs price scatter plot
plt.figure(figsize=(8,5))

sns.boxplot(x="Rating", y="Price", data=df)

plt.title("Rating vs Price")

plt.show()
# calculate average price by rating
print(df.groupby("Rating")["Price"].mean())
# visualization of average price by ratings
plt.figure(figsize=(8,5))
sns.barplot(x="Rating", y="Price", data=df)

plt.title("Average Price by Rating")

plt.show()
# correlation between price and rating
print(df.corr(numeric_only=True))
# heatmap to visualize the correlation between price and rating
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")

plt.show()
# detecting data issues
print(df.isnull().sum())
# dulipicated row 
print(df.duplicated().sum())
# outliers in price column
sns.boxplot(x=df["Price"])
print(df.dtypes)
print(df["Rating"].unique()) # rating values 
# top 10 most  expensive books
top_books = df.sort_values(
    by="Price",
    ascending=False
).head(10)

print(top_books)
# price stat
print(df["Price"].describe())