import requests
import json

content =  []

client_id = '4c7d7b4713478c029c80'
client_secret = 'c2d5bacd6e38a0ce71eaa90e30d93b0e'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open('dataset_24476_4.txt', 'r', encoding='utf-8') as file:
    ids = [id.rstrip() for id in file.readlines()]

for id in ids:
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)
    r.encoding = 'utf-8'

    # разбираем ответ сервера
    j = json.loads(r.text)
    content.append((int(j['birthday']), j['sortable_name']))

with open('result.txt', 'w', encoding='utf-8') as file:
    sorted_content = sorted(content, key=lambda para: (para[0], para[1]))
    for el in sorted_content:
        file.write(f'{el[1]}\n')
        # file.write(f'{el[0]}, {el[1]}\n')

