a = 1
b = 2
c = 1

my_condition = a < b
print(my_condition)
if my_condition:
    print('a es menor que b')

if a < b:
    print('un if de toda la vida')
else:
    print('b es menor que a')

if a < b and b > c:
    print('a es menor que b y b es mayor que c')

if (a > b) or (c < b and c == a):
    print('lol, como te complicas')



# Cuando hay un and, todo tiene que ser True. Para or vale con que uno sea cierto.

# Buenas prácticas: usar if en positivo. Cuanto menos not mejor