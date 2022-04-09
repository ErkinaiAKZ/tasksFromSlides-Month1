#списки
#problem 1:

list = ['city', 25, 0.60, True, ('state')]
print(list)

#problem 2:

NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK',
'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON']

print(NAMES.count('JACK'))

#problem 3:

NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON','JHON','JIMMY','JACKSON', 'JHON','JACK',
         'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK','JIMMY', 'JACK', 'JACKSON', 'JHON']

del NAMES[0:10:2]
print(NAMES)

#problem 4:

lst = []
lst.append('Erkinai')
lst.append(1994)
lst.append('python')

print(lst)

#problem 5:

lst = ['bishkek', 'talas', 'osh', 'naryn', 'tokmok']

all_cities = ' '.join(lst)

print(all_cities)

