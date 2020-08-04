from math import e
def func(n):
    return round(e,n)

n = int(input('Enter a whole num upto which decimals you want e '))
ans = func(n)
print(f'e upto {n} decimal place is {ans}')