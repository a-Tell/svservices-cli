from bs4 import BeautifulSoup
import requests

url = 'https://swisscom-fiftyone.sv-restaurant.ch/de/menuplan/'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html5lib')
today = soup.find('div', attrs = {'id':'menu-plan-tab1', 'class':'menu-plan-grid'})
menus_today = today.find_all('div', attrs = {'class':'menu-item'})

for row in menus_today:
    print(row.find('span', attrs={'class': 'menuline'}).text,':')
    print("---")
    print(row.find('h2', attrs = {'class': 'menu-title'}).text)
    description = row.find('p', attrs={'class': 'menu-description'}).text.replace("\n", " ")
    print(description)
    print("---")