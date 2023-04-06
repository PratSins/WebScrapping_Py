import requests
import bs4

# The commented part of the code prints the source code of the requested webpage

print()
result = requests.get("http://www.example.com")
print("Type of value returned by requests.get()  -->",type(result))
# print("\n ______________Source Code of the webpage________________________\n")
# print(result.text)
print("\n\n")

soup = bs4.BeautifulSoup(result.text,"lxml")
# print("SOUP(Source Code of the webpage) ---\n", soup)


print("soup.select('title')   ---->",soup.select('title'))
print("soup.select('h1')   ---->",soup.select('h1'))

print()
print("soup.select('title')[0]   ---->",soup.select('title')[0])
print("soup.select('title')[0].getText()   ---->",soup.select('title')[0].getText())
print()


site_paragraphs = soup.select("p")
print("type(site_paragraphs)  --->",type(site_paragraphs),"\n\n")
print("site_paragraphs[0]  ---> ",site_paragraphs[0])
print("site_paragraphs[1]  ---> ",site_paragraphs[1])
print()
print("site_paragraphs[0].getText()  ---> ",site_paragraphs[0].getText())
print("site_paragraphs[1].getText()  ---> ",site_paragraphs[1].getText())