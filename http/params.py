import requests as req
url = "https://icanhazdadjoke.com/search"
res = req.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': 'cat', 'limit': 5}
)
data = res.json()
for i in data['results']:
    print(i)
