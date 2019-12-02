from bs4 import BeautifulSoup
import csv
import requests
from time import sleep


url = 'https://rithmschool.com'
counter = 1
with open('rithm_all_pages.csv', 'w') as file:
    csv_w = csv.writer(file)
    csv_w.writerow(['title', 'link', 'date'])
    while counter <= 9:
        page = '/blog?page=' + str(counter)
        res = requests.get(url+page)
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.find_all('article')
        for art in articles:
            a_tag = art.find('a')
            title = a_tag.get_text()
            link = a_tag['href']
            date = art.find('time')['datetime']
            csv_w.writerow([title, link, date])
        sleep(1)
        counter += 1



