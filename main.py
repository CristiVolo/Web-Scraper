from bs4 import BeautifulSoup
import requests


search = input("Search for")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, features="html.parser")
results = soup.find("ol", attrs={"id": "b_results"})
links = results.findAll("li", attrs={"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print("\n")
        print(item_text)
        print(item_href)

        print("Summary:", item.find("a").parent.parent.find("p").text)

        child = item.find("h2")
        print(child, "\nThe next sibling of h2 is:", child.next_sibling)
        children = item.children
        for child in children:
            print("Child:", child)


# print(soup.prettify())
