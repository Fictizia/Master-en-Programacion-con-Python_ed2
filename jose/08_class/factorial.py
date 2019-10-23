# n! result = n*n-1
# result*n-2 
# result....----- (n-(n-1)) == 1

def factorial(n):
    result = n
    for n in range(n,1,-1):
        result *= n-1
    print(result)

factorial(3)

def factor_recur(n):
    if n != 0:
        return n * factor_recur(n-1)
    return 1

print(factor_recur(3))