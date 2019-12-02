from csv import DictWriter
from bs4 import BeautifulSoup
from requests import get
from time import sleep

#
# url = 'http://quotes.toscrape.com'
# res = get(url)
# with open('quotes.csv', 'w') as file:
#     headers = ['text', 'author', 'link']
#     csv_w = DictWriter(file, fieldnames=headers)
#     csv_w.writeheader()
#     while True:
#         soup = BeautifulSoup(res.text, 'html.parser')
#         try:
#             quotes = soup.find_all(class_='quote')
#             for quote in quotes:
#                 csv_w.writerow({
#                     'text': quote.find(class_="text").get_text(),
#                     'author': quote.find(class_="author").get_text(),
#                     'link': quote.find("a")["href"]
#                 })
#             page = soup.find(class_='next').find('a')['href']
#             res = get(url+page)
#         except:
#             break

url = 'http://quotes.toscrape.com'
page = '/page/1/'
with open('quotes_1.csv', 'w') as file:
    headers = ['text', 'author', 'link']
    csv_w = DictWriter(file, fieldnames=headers)
    csv_w.writeheader()
    while page:
        res = get(url+page)
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(class_='quote')
        for quote in quotes:
            csv_w.writerow({
                'text': quote.find(class_='text').get_text(),
                'author': quote.find(class_='author').get_text(),
                'link': quote.find('a')['href']
            })
        nxt_btn = soup.find(class_='next')
        page = nxt_btn.find('a')['href'] if nxt_btn else None
        sleep(1)

