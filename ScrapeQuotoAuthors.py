# www.toscrape.com
import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")   # will give error if the website is not accessible
soup = bs4.BeautifulSoup(res.text,"lxml")

authors = set()

for name in soup.select(".author"):
    authors.add(name.text)

print(authors)
print()

k= soup.select(".text")

quotes = []
for quote in k:
    quotes.append(quote.text)

print(quotes)
print()

for item in soup.select(".tag-item"):
    print(item.text)
print()


url = 'http://quotes.toscrape.com/page/'
authors = set()

for page in range(1,10):
    page_url = url+str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)
