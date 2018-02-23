import requests


resp = requests.get('https://httpbin.org/ip')

print('Your IP is {}'.format(resp.json()['origin']))
