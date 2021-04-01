from bs4 import BeautifulSoup
import os

url = "index.html"
page = open(url)
soup = BeautifulSoup(page, 'html.parser')

os.system('clear')
# print(soup.title)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
print(soup.get_text())