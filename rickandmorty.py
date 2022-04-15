
from pprint import pprint as pp
import requests

r = requests.get('https://rickandmortyapi.com/api/character/?name=morty').json()
pp(f"имя: {r['results'][0]['name']}")
pp(f"статус: {r['results'][0]['status']}")
pp(f"спецификация: {r['results'][0]['species']}")
pp(f"тип: {r['results'][0]['type']}")
pp(f"гендер: {r['results'][0]['gender']}")
pp(f"картинка: {r['results'][0]['image']}")
pp(f"эпизод: {r['results'][0]['episode']}")
pp(f"локация: {r['results'][0]['location']}")

print('--------------------')

r2 = requests.get('https://rickandmortyapi.com/api/character/283').json()
pp(f"имя: {r2['name']}")
pp(f"статус: {r2['status']}")
pp(f"спецификация: {r2['species']}")
pp(f"статус: {r2['status']}")
pp(f"тип: {r2['type']}")
pp(f"гендер: {r2['gender']}")
pp(f"картинка: {r2['image']}")
pp(f"эпизод: {r2['episode']}")
pp(f"локация:: {r2['location']}")

print('--------------------')

r3 = requests.get('https://rickandmortyapi.com/api/character/?name=summer smith').json()
pp(f"имя: {r3['results'][0]['name']}")
pp(f"статус: {r3['results'][0]['status']}")
pp(f"спецификация: {r3['results'][0]['species']}")
pp(f"тип: {r3['results'][0]['type']}")
pp(f"гендер: {r3['results'][0]['gender']}")
pp(f"картинка: {r3['results'][0]['image']}")
pp(f"эпизод: {r3['results'][0]['episode']}")
pp(f"локация:: {r3['results'][0]['location']}")

print('--------------------')

r4 = requests.get('https://rickandmortyapi.com/api/character/?name=jerry smith').json()

pp(f"имя: {r4['results'][0]['name']}")
pp(f"статус: {r4['results'][0]['status']}")
pp(f"спецификация: {r4['results'][0]['species']}")
pp(f"тип: {r4['results'][0]['type']}")
pp(f"гендер: {r4['results'][0]['gender']}")
pp(f"картинка: {r4['results'][0]['image']}")
pp(f"эпизод: {r4['results'][0]['episode']}")
pp(f"локация:: {r4['results'][0]['location']}")

print('--------------------')

r5 = requests.get('https://rickandmortyapi.com/api/character/?name=squanchy').json()

pp(f"имя: {r5['results'][0]['name']}")
pp(f"статус: {r5['results'][0]['status']}")
pp(f"спецификация: {r5['results'][0]['species']}")
pp(f"тип: {r5['results'][0]['type']}")
pp(f"гендер: {r5['results'][0]['gender']}")
pp(f"картинка: {r5['results'][0]['image']}")
pp(f"эпизод: {r5['results'][0]['episode']}")
pp(f"локация:: {r5['results'][0]['location']}")

print('--------------------')

r6 = requests.get('https://rickandmortyapi.com/api/character/?name=beth smith').json()

pp(f"имя: {r6['results'][0]['name']}")
pp(f"статус: {r6['results'][0]['status']}")
pp(f"спецификация: {r6['results'][0]['species']}")
pp(f"тип: {r6['results'][0]['type']}")
pp(f"гендер: {r6['results'][0]['gender']}")
pp(f"картинка: {r6['results'][0]['image']}")
pp(f"эпизод: {r6['results'][0]['episode']}")
pp(f"локация:: {r6['results'][0]['location']}")

print('--------------------')

r7 = requests.get('https://rickandmortyapi.com/api/character/?name=Krombopulos Michael').json()

pp(f"имя: {r7['results'][0]['name']}")
pp(f"статус: {r7['results'][0]['status']}")
pp(f"спецификация: {r7['results'][0]['species']}")
pp(f"тип: {r7['results'][0]['type']}")
pp(f"гендер: {r7['results'][0]['gender']}")
pp(f"картинка: {r7['results'][0]['image']}")
pp(f"эпизод: {r7['results'][0]['episode']}")
pp(f"локация:: {r7['results'][0]['location']}")

print('--------------------')

r8 = requests.get('https://rickandmortyapi.com/api/character/?name=Reverse Giraffe').json()
pp(f"имя: {r8['results'][0]['name']}")
pp(f"статус: {r8['results'][0]['status']}")
pp(f"спецификация: {r8['results'][0]['species']}")
pp(f"тип: {r8['results'][0]['type']}")
pp(f"гендер: {r8['results'][0]['gender']}")
pp(f"картинка: {r8['results'][0]['image']}")
pp(f"эпизод: {r8['results'][0]['episode']}")
pp(f"локация:: {r8['results'][0]['location']}")

print('--------------------')

r9 = requests.get('https://rickandmortyapi.com/api/character/?name=Birdperson').json()

pp(f"имя: {r9['results'][0]['name']}")
pp(f"статус: {r9['results'][0]['status']}")
pp(f"спецификация: {r9['results'][0]['species']}")
pp(f"тип: {r9['results'][0]['type']}")
pp(f"гендер: {r9['results'][0]['gender']}")
pp(f"картинка: {r9['results'][0]['image']}")
pp(f"эпизод: {r9['results'][0]['episode']}")
pp(f"локация:: {r9['results'][0]['location']}")
