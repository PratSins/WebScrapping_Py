# www.toscrape.com
import requests
import bs4


base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# # test code
# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# products = soup.select(".product_pod")

# for i in products:
#     print(i)
# print(len(products))

# print(products[0])
# print("star-rating Three" in str(products[0]))

# exp = products[0]
# print(exp.select(".star-rating.Three"))    # if there is a whitespace in between replace it with dot(.)

# k = exp.select("a")[1]['title']
# print(k)


two_star_titles = []
for n in range(1,51):
    print("---Page ",n,"---")
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        #if 'star-rating Two' in str(book)
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
