import requests as req
url = 'http://www.google.com'
res = req.get(url)
print(f'your request to {url} came back '
      f'with status code {res.status_code}')