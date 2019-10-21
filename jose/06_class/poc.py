def a():
    if True:
        return 1, 2
    a()

x,y = a()

print(x)
print(y)