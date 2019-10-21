# La sucesión comienza con los números 0 y 1, 2
# A partir de estos, cada término es la suma de los dos anteriores


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


result = fibonacci(9)
print(result)
