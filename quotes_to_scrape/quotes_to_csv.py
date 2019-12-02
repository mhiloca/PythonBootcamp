from requests import get
from bs4 import BeautifulSoup
from csv import DictWriter
import re

url = 'http://quotes.toscrape.com'
page = '/page/1/'
while page:
    res = get(url+page)
    soup = BeautifulSoup(res.text, 'html.parser')
    with open('quotes_file.csv', 'a') as file:
        headers = ['author', 'text', 'hint_born', 'hint_gender', 'hint_text']
        writer = DictWriter(file, fieldnames=headers)
        writer.writeheader()
        quotes = soup.find_all(class_='quote')
        for quote in quotes:
            res_author = get(url+quote.find('a')['href'])
            soup_author = BeautifulSoup(res_author.text, 'html.parser')
            name = quote.find(class_='author').get_text()
            fullname = name.split()
            first, last = fullname[0].strip(), fullname[1].strip()
            hint_date = soup_author.find(class_='author-born-date').get_text()
            hint_local = soup_author.find(class_='author-born-location').get_text()
            description_text = soup_author.find(class_='author-description').get_text()
            gender = ''
            she = re.compile(r'\b(she|her)\b', re.I)
            he = re.compile(r'\b(he|his)\b', re.I)
            if she.search(description_text):
                gender = 'woman'
            elif he.search(description_text):
                gender = 'man'
            hint_text = description_text.split()[20:50]
            hint_text = ' '.join(hint_text)
            name_subs = re.compile(r'\b('+first+r'|'+last+r')\b')
            writer.writerow({
                'author': name,
                'text': quote.find(class_='text').get_text(),
                'hint_born': hint_date + ' ' + hint_local,
                'hint_gender': f'The author is a {gender}',
                'hint_text': f'... {name_subs.sub("-AUTHOR-",hint_text)}...'
            })
        next_btn = soup.find(class_='next')
        page = next_btn.find('a')['href'] if next_btn else None
