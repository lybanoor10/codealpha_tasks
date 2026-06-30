import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

titles = []
prices = []
availability_list = []
ratings = []

for page in range(1, 51):

    print(f"Scraping page {page}")

    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:

            title = book.h3.a["title"]

            price = book.find("p", class_="price_color").text

            availability = (
                book.find(
                    "p",
                    class_="instock availability"
                ).text.strip()
            )

            rating = book.find("p")["class"][1]

            titles.append(title)
            prices.append(price)
            availability_list.append(availability)
            ratings.append(rating)

    else:
        print(f"Failed to access page {page}")

    time.sleep(1)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Availability": availability_list,
    "Rating": ratings
})

print(df.head())

df.to_csv("all_books.csv", index=False)

print("\nDataset saved successfully!")
print("Total books scraped:", len(df))