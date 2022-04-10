#Исключения
#problem 1:

a = int(input('enter a number:'))
b = 'error'

print(a - b)          # TypeError
print(b[87])          #IndexError
print(c)              #NameError

#problem 2:

at = 10
fin = 15
wo = 20
try:
    for e in range(-at, at):
        print(wo / e)
        if at > '5':
            print("at > 5")
except SyntaxError:
    print('SyntaxError occured')
except NameError:
    print('NameError occured')
except TypeError:
    print('TypeError occured')
except ZeroDivisionError:
    print('ZeroDivisionError occured')

#problem 3:

lst = []
try:
    for i in range(10):
        lst.append(i)
    a = reversed(lst)
    sls_obj = slice('0','8')
    print(а[sls_obj])
except Exception:
    print('Something went wrong')

#problem 4:

a = 0
b = 1
numbers = []
try:
    while b > a:
        numbers += b
        b += 1
except TypeError:
    print('TypeError occured')
