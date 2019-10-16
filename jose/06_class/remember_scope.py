a = 1

def test_scope():
    print(a)
    b = 2
    def test_test_scope():
        print(a)
        print(b)
    return b

c = test_scope()
print(c)