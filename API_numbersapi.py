import requests

with open('dataset_24476_3.txt', 'r', encoding='utf-8') as file:
    content = [i.strip() for i in file.readlines()]

for el in content:
    api_url = f'http://numbersapi.com/{el}/math?json'
    params = {
        'json': True
    }

    res = requests.get(api_url, params=params)
    data = res.json()
    print('Interesting' if data['found'] else 'Boring')