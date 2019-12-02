import requests

url = 'https://weather.com'
res = requests.get(url)

# print(res.headers)
print(f'Your request to {url} came back with status code {res.status_code}')

