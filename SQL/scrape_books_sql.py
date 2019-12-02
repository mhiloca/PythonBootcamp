import sqlite3
from bs4 import BeautifulSoup
from requests import get
from time import sleep


def scrape_books(url, page):
    all_books = []
    while page:
        res = get(url + page)
        soup = BeautifulSoup(res.text, 'html.parser')
        books = soup.find_all('article')
        for book in books:
            data = (get_title(book), get_price(book), get_rating(book))
            all_books.append(data)
        next_btn = soup.find(class_='next')
        page = next_btn.find('a')['href'] if next_btn else None
        sleep(1)
    books_data(all_books)


def get_title(book):
    return book.find('h3').find('a')['title']


def get_price(book):
    price = book.select('.price_color')[0].get_text()
    return float(price.replace('Â', '').replace('£', ''))


def get_rating(book):
    rate = book.find('p')['class']
    stars = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    return stars[rate[-1]]


def books_data(all_books):
    connection = sqlite3.connect('books_scraper.db')
    c = connection.cursor()
    c.execute('CREATE TABLE books (title TEXT, price REAL, rate INTEGER)')
    c.executemany('INSERT INTO books VALUES (?, ?, ?)', all_books)
    connection.commit()
    connection.close()


url = 'http://books.toscrape.com/catalogue/'
page = 'page-1.html'
scrape_books(url, page)
