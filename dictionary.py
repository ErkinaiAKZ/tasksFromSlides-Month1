#словари

#problem 1:

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
a = {"drinks": ['Coca-Cola', 'Sprite', 'Fanta']}
menu.update(a)
print(menu)

#problem 2:

dict1 = {}
x = 0 
while x < 3:
    
    x += 1
    y = input('введите имя:')
    z = input('введите пароль:')
    dict1[y] = z
    print(dict1)

#problem 3:

dict2 = {'Sam': 'ceo', 'Lena': 'secretary', 'Aza': 'driver', 'John': 'staff','Alex': 'manager'}

for name, prof in dict2.items():
    print('Здравствуйте', name, 'прекрасная профессия', prof)

#problem 4:
#№1

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
a = {'besh_barmak': 130}
menu.update(a)
print(menu)

#№2

menu = {'lagman': 120, 'plov': '120', 'borsh': 100, 'besh_barmak': 130}
menu['lagman'] = 135
print(menu)

#№3

menu = {'lagman': 120, 'plov': '120', 'borsh': 100, 'besh_barmak': 130}
del menu['borsh']
print(menu)

#problem 5:

south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile','Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru',
                        'Suriname','Suriname', 'Uruguay', 'Venezuela']

sac2 = list(dict.fromkeys(south_american_countries))
print(sac2)
sac3 =dict(zip (range(len(sac2)), sac2))
print(sac3)