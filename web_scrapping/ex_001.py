import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.rithmschool.com/blog'
response = requests.get(url)
data = BeautifulSoup(response.text, 'html.parser')
articles = data.find_all("article")
"""
links, texts, dates = [], [], []
for art in articles:
    links.append(art.find("a")["href"])
for art in articles:
    texts.append(art.select("[href]")[0].get_text())
for art in articles:
    dates.append(art.find("small").get_text())
with open('exercise_rithmblog.csv', 'w') as file:
    csv_w = csv.writer(file)
    csv_w.writerow(['link', 'title', 'date'])
    for index in range(len(links)):
        csv_w.writerow([links[index], texts[index], dates[index].replace(',', '')])
"""
with open('exercise_rithmblog_2.csv', 'w') as file:
    csv_w = csv.writer(file)
    csv_w.writerow(['title', 'href', 'date'])
    for art in articles:
        a_tag = art.find("a")
        title = a_tag.get_text()
        href = a_tag("a")["href"]
        date = art.find("time")["datetime"]
        csv_w.writerow([title, href, date])
