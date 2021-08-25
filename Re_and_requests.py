# Задание из курса Python: основы и применение.
# https://stepik.org/lesson/24471/step/6?unit=6780

import re
import requests


a, b = input().rstrip(), input().rstrip()
pattern = r'<a href="(\S+?)">'
response = requests.get(a)
links = re.findall(pattern, response.text)
urls = []
for link in links:
    res = requests.get(link)
    urls.extend(re.findall(pattern, res.text))
print('Yes' if b in urls else 'No')