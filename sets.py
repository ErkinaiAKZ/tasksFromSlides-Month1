#множества

#problem 0:

dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}

dates_of_birth.discard(6)

print(dates_of_birth)

#problem 1:

x = frozenset({12, 56, 7})
y = frozenset({4, 8, 13})
z = frozenset({90, 78, 123})
a = set([x, y, z])
print(a)

#problem 2:

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

result = farm_2.difference(farm_1)
print(result)

#problem 3:

set_1 ={45, 'car', 'coffee', 3567, 'cakes'}
set_1.add(55)
print(set_1)
set_1.pop()
print(set_1)

#problem 4:

my_set = set()

for digit in range(10):
    enter_digit = int(input('Введите число:'))
    my_set.add(enter_digit)

fr_set = frozenset(my_set)
print(fr_set)

#problem 5:

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

common = farm_2.intersection(farm_1)
print(common)

difference = farm_1.difference(farm_2)
print(difference)