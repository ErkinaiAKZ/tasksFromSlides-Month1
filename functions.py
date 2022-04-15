# Функции
#Problem 1:

list_1 = ['name', 'age', '1', '19']
    
def reverse(value):
    first_part = value[:len(value)//2][::-1]    
    second_part = value[len(value)//2:][::-1]
    return first_part + second_part

print(reverse(list_1))

#Problem 2:

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + (n - 2)

for i in range(1, 11):
    print(fib(i), end=', ')

#Problem 3:

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def rec_sum_difference(c, d):
    print(sum(c, d), difference(c, d))

rec_sum_difference(20, 40)

#Problem 4:

name_of_file = input('введите имя файла:')

def create_file(n):
    file_name = f'{n}.txt'
    with open(file_name, 'w') as f:
        f.write('File Created')
    return 'File Created'

file = create_file(name_of_file)
print(file)

#Problem 5:

from random import choice

def gen_num():
    code = '0444'
    numbers = '145790'
    for num in range(6):
        code += choice(numbers)
    return code

print(gen_num())
print(gen_num())
print(gen_num())

#Problem 6:

def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n = int(input('Введите число:'))
if (check(n) == True):
    print('Число четное!')
else:
    print('Число нечетное!')

#Problem 7:

set1 = {4, 6, 98, 234, 6, 45, 564}

def del_item_of_set(s):
    return (set1.pop())

print(set1)
print(del_item_of_set(set1))
print(del_item_of_set(set1))
print(set1)
