from math import pi
def func(n):
    return round(pi,n)

n = int(input('Enter a whole num upto which decimals you want pi '))
ans = func(n)
print(f'Pi upto {n} decimal place is {ans}')