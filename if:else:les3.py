#lesson3 if/else/elif
#problem 1:

a = 2 ** 3
b = 3 ** 2
if a > b:
    print('a:', a)
else:
    print('b:', b)

#problem 2:

a = 5
b = 70
c = 28

if a > b and a > c:
    print('Самое большое число: a')
elif b > a and b> c:
    print('Самое большое число: b')
else:
    print('Самое большое число: c')

if a < b and a < c:
    print('Самое маленькое число: a')
elif b < a and b < c:
    print('Самое маленькое число: b')
else:
    print('Самое маленькое число: c')

#problem 3:

y = 17391 % 17
x = 546 % 17
z = 934 % 17

if y < x and y < z:
    print('Остаток меньше всего в y:', y)
if x < y and x < z:
    print('Остаток меньше всего в x:', x)
if z < x and z < y:
    print('Остаток меньше всего в z', z)


#problem 4:

x = 13**2

if x < 172:
    x = x ** 2
    print(x)

#problem 5:

integer = int(input("Введите число:"))
if integer % 2 == 0 and integer % 3 == 0 and integer ** 2 > 1000:
    print('Ваше число четное, делится на 3 без остатка, если возвести его в квадрат, оно больше 1000')
else:
    print('Ваше число не соответствует критериям')

#problem 6:

n = int(input("enter number from 0 to 100: "))

if 0 > n < 21 or 57 > n < 100:
    print("allowed!")
else:
    print("not allowed!")

#problem 7:
a = True
if a < 10:
    print(a + 10)

#problem 8:

interview = input('Введите True или False:')
exam_score = int(input('Введите результат экзаменации:'))
age = int(input('Введите Ваш возраст:'))
counter = 0

if interview == 'True':
    counter += 1
    if exam_score >= 90:
        counter += 1
        if age > 18:
            counter += 1

if counter == 3:
    print('Вы приняты на работу')
else:
    print('Не подходите')

#problem 9:

a = 10//5
b = 10/5
c = a + b

if a == b:
    print(c)
else:
    print('not equal')

#problem 10:

digit = int(input('введите число:'))

if digit < 0:
    print(digit)
else:
    print('не отрицательное')

#problem 11:

a = 10
b = 5

if a > 0 and b > 0:
    print("положительные")
else:
    print('отрицательные')

#problem 12:

a = 10
b = 5

if a > b:
    print(a+2)
    if b > a:
        print(b+2)
