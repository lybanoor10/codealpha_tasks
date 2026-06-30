#  for total books count
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
#  for books name



url = "http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")

for book in books:
    print(book.a["title"])
    
#  for extract prices of books

url = "http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    print(title)
    print(price)
    print("-" * 50)
    #  store data is lists

import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    titles.append(title)

    prices.append(price)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

print(df)
#  store data in csv file
df.to_csv("books.csv", index=False)

print("Dataset saved successfully!")