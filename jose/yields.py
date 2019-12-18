# yield aka generator objects


num_list = [num*num for num in range(3)]

for num in num_list:
    print(num)

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)