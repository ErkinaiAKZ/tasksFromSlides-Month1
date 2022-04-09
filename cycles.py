#Циклы

#problem 1:
lang1 = 'Rust'
languages = ['Rust','go', 'java', 'php', 'python', 'javascript', 'ruby']

for item in languages:
    if lang1 == item:
        print('this language is in list')

#problem 2:

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for lan in languages:
    print(lan)
    if lan == 'php':
        break

#problem 3:

x = 7

for i in range(5):
    x = x * x
    print(x)

#problem 4:

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

length = len(languages)
for i in range(length):
    print(i, languages[i], end= ' ')

#2nd version:
for i, elem in enumerate(languages):
    print(i, elem)

#problem 5:

for i in range (1,10):
    print(i, end = ' ')
for a in range (10, 0, -1):
    print(a, end = ' ')

print('\n')
#2nd task:

start = 1
end = 10

while True:
    if start < 10:
        print(start, end =' ')
        start += 1
    elif start >= 10:
        print (end, end = ' ')
        end -= 1
        if end == 0:
            break

#problem 6:

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')

for i in range (len(names)):
    if i % 2 == 0:
        print(names[i], end = ' ')

print('\n')

#problem 7:

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)

for i in range(0, len(names), 2):
    print(names[i], end = ' ', )

#problem 8:

digit = 600

if digit >= 100 and digit < 1000:
    print('Это число трёхзначное.')
    if digit >0 and digit % 2 == 0:
        print('Это число положительное и чётное.')
        if digit % 31 == 0:
            print('Это число делится на 31 без остатка.')
            if digit > 100 and digits % 17 == 0 or digit > 150 and digit == 13**2:
                print('digit')

#problem 9:

counter1 = 0

for i in range (-100, 100):
    if i % 13 ==0 and i % 2 ==0:
        i = i ** 2
        print(i, end=' ')
        counter1 += 1
print('\n')

counter2 = 0
for a in range(-100, 100, 7):
    if a % 2 != 0:
        print(a, end= ' ')
        counter2 += 1
print('\n')

print('Под первое условие подходят', counter1, 'чисел')
print('Под первое условие подходят', counter2, 'чисел')
