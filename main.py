from bs4 import BeautifulSoup
import requests


search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/search?q=pizza", params=params)

soup = BeautifulSoup(r.text, features="html.parser")
print(soup.prettify())
