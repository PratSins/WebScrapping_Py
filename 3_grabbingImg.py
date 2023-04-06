import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)
# print(res.text)

img = soup.select("img")

for i in img:
    #print(i)
    print(i.attrs["src"])
print()

k = soup.select(".thumbimage")

for i in k:
    # print(i)
    print(i.attrs["src"])
    
# do add the "http:" in the beginning to avoid error
img_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")
# print(img_link.content)


f = open("computer_image.jpg", 'wb')   # wb --> write binary
print(f.write(img_link.content))  
# f.write() can be exected without print() but I did it here to see the integer value returned
f.close()