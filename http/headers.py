import requests as req
url = "https://icanhazdadjoke.com"
"""res = req.get(
    url, headers={'Accept': 'text/plain'}
)
print(res.text)
"""
res = req.get(
    url,
    headers={'Accept': 'application/json'}
)
# print(type(res.text))
data = res.json()
print(data['joke'])
