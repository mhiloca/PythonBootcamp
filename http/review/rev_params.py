import requests

url = 'https://icanhazdadjoke.com/search'
response = requests.get(
    url,
    headers={'Accept': 'application/json'},
)
data = response.json()
for key, value in data.items():
    print(f'{key}: {value}')
