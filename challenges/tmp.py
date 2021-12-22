import requests

url = 'https://jsonmock.hackerrank.com/api/food_outlets'

req = requests.get(url).json()
pages = req['total']
name = req['data'][0]['name']
cost = req['data'][0]['estimated_cost']

print(pages)

print(name)

