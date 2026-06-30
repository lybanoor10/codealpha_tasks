import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("clean_books.csv")
#  which ratings are most common
plt.figure(figsize=(8,5))

sns.countplot(x="Rating", data=df)

plt.title("Distribution of Book Ratings")

plt.xlabel("Rating")

plt.ylabel("Number of Books")

plt.show()
# price distribution of books
plt.figure(figsize=(10,6))

sns.histplot(df["Price"], bins=20)

plt.title("Distribution of Book Prices")

plt.xlabel("Price (£)")

plt.ylabel("Number of Books")

plt.show()
# top 10 most expensive books
top10 = df.sort_values(
    "Price",
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x="Price",
    y="Title",
    data=top10
)

plt.title("Top 10 Most Expensive Books")

plt.show()
# average price by rating
avg_price = df.groupby("Rating")["Price"].mean().reset_index()

plt.figure(figsize=(8,5))

sns.barplot(
    x="Rating",
    y="Price",
    data=avg_price
)

plt.title("Average Price by Rating")

plt.show()
#  price box plot 
plt.figure(figsize=(10,4))

sns.boxplot(x=df["Price"])

plt.title("Book Price Outliers")

plt.show()
# rating pie chart
rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct="%1.1f%%"
)

plt.title("Book Rating Distribution")

plt.show()
# correlation heatmap
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.show()
# saving  charts as images
plt.savefig(
    "rating_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
import os

os.makedirs("images", exist_ok=True)
plt.figure(figsize=(8,5))

sns.countplot(x="Rating", data=df)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.savefig("images/rating_distribution.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()
plt.figure(figsize=(10,6))

sns.histplot(df["Price"], bins=20)

plt.title("Price Distribution")

plt.savefig("images/price_distribution.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()
plt.figure(figsize=(12,6))

sns.barplot(x="Price", y="Title", data=top10)

plt.title("Top 10 Most Expensive Books")

plt.savefig("images/top10_expensive_books.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()
plt.figure(figsize=(8,5))

sns.barplot(x="Rating", y="Price", data=avg_price)

plt.title("Average Price by Rating")

plt.savefig("images/average_price_by_rating.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()
plt.figure(figsize=(8,5))

sns.boxplot(x=df["Price"])

plt.title("Price Outliers")

plt.savefig("images/price_boxplot.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()
plt.figure(figsize=(6,5))

sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.title("Correlation Heatmap")

plt.savefig("images/correlation_heatmap.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()
plt.figure(figsize=(7,7))

plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct="%1.1f%%"
)

plt.title("Rating Distribution")

plt.savefig("images/rating_pie_chart.png", dpi=300, bbox_inches="tight")

plt.show()

plt.close()