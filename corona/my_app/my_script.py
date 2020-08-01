import os
import django
import requests
from datetime import datetime 
from bs4 import BeautifulSoup
from my_app.models import Stats,News
def populate_stat():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','corona.settings')
    django.setup()
    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    spans = soup.findAll('div',{'class':'maincounter-number'})
    lis = []
    for i in spans:
        lis.append((i.find('span').text))
    print('table1 updating ..... ... ...')
    s = Stats.objects.get_or_create(total_cases=lis[0],deaths=lis[1],recovered_cases=lis[2],new_date=datetime.now())[0]
    s.save()
    print('table1 updated......')

def populate_news():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','corona.settings')
    django.setup()

    url = "https://www.indiatoday.in/coronavirus-covid-19-outbreak?page=&view_type=list"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    contain = soup.findAll('div',{'class':'detail'})
    news= []
    links = []
    for i in contain:
        a = i.find('a')
        href = 'https://www.indiatoday.in'+ a['href']
        news.append(i.text)
        links.append(href)
    print('table2 updating ..... ... ...')
    for i in range(len(news)):
        n = News.objects.get_or_create(headline=news[i],link=links[i])[0]
        n.save()
    print('table2 updated......')

