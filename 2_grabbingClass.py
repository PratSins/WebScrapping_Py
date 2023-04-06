import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(res.text,"lxml")
# print(res.text)
# print(soup)

k = soup.select('.infobox-label')
# here we are trying to get the the class atrribute different labels based on their value, here it's ''' infobox-label  '''
# the dot(.) added before the label value to signal that its for grabbing a class with value

print(k)
print()

print(k[0])
print(k[0].text)
print()

for item in k:
    print(item.text)
