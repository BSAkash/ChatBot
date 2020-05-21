#!/usr/bin/env python
import requests

res = requests.get('https://rikilg.pythonanywhere.com/test')
print(res.text)
x = input('query> ')
while x != "":
    res = requests.post('https://rikilg.pythonanywhere.com/api/', json={
        'query': x
    })
    print('bot>', res.json()['response'])
    x = input("query> ")