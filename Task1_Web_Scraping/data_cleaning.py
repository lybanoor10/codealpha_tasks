import pandas as pd
df = pd.read_csv("all_books.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
# df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].str.extract(r'(\d+\.\d+)')[0]
df["Price"] = pd.to_numeric(df["Price"])
print(df.dtypes)
print (df.dtypes["Price"])
# ratings  dictionary formation 
rating_map = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}
df["Rating"] = df["Rating"].map(rating_map)
# statistics examination
print(df.describe())
# price catogory formation

def price_category(price):

    if price < 20:
        return "Low"

    elif price < 40:
        return "Medium"

    else:
        return "High"
df["Price_Category"] = df["Price"].apply(price_category)
print(df.head())
df.to_csv("clean_books.csv", index=False)

print("Clean dataset saved successfully!")