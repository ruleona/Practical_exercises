import requests

city = input('City?')
api_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': '8c5e184a5a076edf6df01a0613c5eb9f',
    'units': 'metric'
}
res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-Type'])
data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))