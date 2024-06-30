import requests
from bs4 import BeautifulSoup
import time,datetime

def write_to_file(news):
    now=datetime.datetime.now()
    f=open('result_news.txt','a')
    for n in news:
        f.write(str(now)+' '+n+'\n')
    f.close()


def extract_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = []
    find_news=[]

    article = soup.find('span', class_="main__big__title")
    news.append(article.contents[1])

    articles = soup.find_all('span', class_="main__feed__title")

    for a in articles:
        news.append(a.contents[1])


    for title in news:
        if 'Демократ' in title or 'Байден' in title or 'финал' in title:
            find_news.append(title)
    return find_news

url = 'https://www.rbc.ru/'

start_time = time.time()
while time.time() - start_time < 4*3600:
    news = extract_news(url)
    write_to_file(news)
    print(news)

    time.sleep(3600)