import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','capstone_project.settings')
import django
django.setup()
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from stock_app.models import Stock
requests.packages.urllib3.disable_warnings()

def stock_scrape():
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://finance.yahoo.com/sector/ms_technology?.tsrc=fin-srch"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all("tr")[1:]

    for row in table:
        ticker = row.find_all('a')[0]
        link = str("https://finance.yahoo.com"+ ticker['href'])
        ticker = ticker.text
        name = row.find('td', {'aria-label' : 'Name'}).text
        price = row.find("td", {"aria-label": "Price (Intraday)"}).text
        price = float(price.replace(',',''))
        stock_datas = Stock()
        stock_datas.ticker = ticker
        stock_datas.link = link
        stock_datas.name = name
        stock_datas.price = price
        stock_datas.save()
    return stock_datas

if __name__ == '__main__':
    print('populating...')
    stock_scrape()
    print('complete!')
