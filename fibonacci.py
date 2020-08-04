def func(n):
    a= 0
    b=1
    l = []
    if n==0:
        print(a)
    elif n==1:
        print(a,b)
    else:
        for x in range(n):
            l.append(str(a+b))
            a=b
            b= int(l[x])
        c = ' '.join(l)
        print('0','1',c)



n = int(input('Enter a  num upto which you want to print fibonacci series '))
func(n)