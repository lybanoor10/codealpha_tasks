import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("clean_books.csv")

# -----------------------------
# SENTIMENT FUNCTION
# -----------------------------
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# -----------------------------
# APPLY SENTIMENT ANALYSIS
# -----------------------------
df["Sentiment"] = df["Title"].apply(get_sentiment)

# -----------------------------
# CHECK DATA
# -----------------------------
print(df.head())
print(df.columns)
print(df["Sentiment"].value_counts())

# -----------------------------
# PLOT 1: SENTIMENT COUNT
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Distribution of Book Titles")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# -----------------------------
# PLOT 2: PIE CHART
# -----------------------------
sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%"
)
plt.title("Overall Sentiment Analysis")
plt.show()

# -----------------------------
# OPTIONAL: SENTIMENT VS RATING
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Rating", hue="Sentiment", data=df)
plt.title("Rating vs Sentiment")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# -----------------------------
# SAVE UPDATED DATASET
# -----------------------------
df.to_csv("books_with_sentiment.csv", index=False)

print("Task 4 Completed Successfully!")