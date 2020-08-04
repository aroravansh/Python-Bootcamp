import sympy
def func(n):
    l=[]
    lst=[]
    for i in range(2,int(n/2)+1):
        if n%i==0:
            l.append(i)
    for i in range(len(l)):
        if sympy.isprime(l[i]):
            lst.append(l[i])
               
    
           
    return lst




    
n = int(input('Enter a  num for which you want the prime factors: '))
ans = func(n)
if ans ==[]:
    print('Sorry no prime factor found!')
else:
    print('Prime factors are :')
    for i in ans:
        print(i)