import requests
url = 'https://rithmschool.com'
counter = 1
page = '/blog?page=' + str(counter)
res = requests.get(url+page)
print(type(counter))
