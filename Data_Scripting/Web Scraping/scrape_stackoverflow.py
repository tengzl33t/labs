import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

os.system('clear')
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'}

qlist = []

# r = requests.get(url, headers= headers)
# print(r)

# url = "https://stackoverflow.com/questions/tagged/python?tab=active&page=2&pagesize=15"

# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.title.text)

# questions = soup.find_all('div', {'class': 'question-summary'})
# print(len(questions))

def obtainQuestion(tag,page):
    url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=active&page={page}&pagesize=15'
    r = requests.get(url, headers= headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'question-summary'})
    for item in questions:
        question = {
        tag: tag,
        'title' : item.find('a',{'class': 'question-hyperlink'}).text,
        # print(title)
        'link' : 'https://stackoverflow.com' + item.find('a',{'class': 'question-hyperlink'})['href'],
        # print(link)
        'votes' : item.find('span',{'class': 'vote-count-post'}).text,
        # print(votes)
        'date' : item.find('span', {'class': 'relativetime'})['title'],
        # print(date)
        }
        qlist.append(question)
    return 

# obtainQuestion('ptyhon', 4)
# print(len(qlist))

for x in range(1,5):
    obtainQuestion('python', x)
    obtainQuestion('java', x)
    
df = pd.DataFrame(qlist)
df.to_csv('sowquestions.csv')


