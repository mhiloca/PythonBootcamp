from bs4 import BeautifulSoup
from requests import get
import re



# url = 'http://quotes.toscrape.com/author/Albert-Einstein/'
# res = get(url)
# soup = BeautifulSoup(res.text, 'html.parser')
# text = soup.find(class_='author-description').get_text()
# with open('albert_einstein.txt', 'w') as file:
#     for line in text.split('. '):
#         file.write(f'{line.strip()}\n')

file_name = 'albert_einstein.txt'
with open(file_name) as file:
    text = file.read()
name_pattern = re.compile(r'Albert Einstein|Einstein|He|\bhe\b')
print(name_pattern.sub('*', text))

