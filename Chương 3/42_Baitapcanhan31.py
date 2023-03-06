import math 
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if(a,b,c >0):
    if(a+b-c>0 and a+c-b>0 and c+b-a>0):
        p=(a+b+c)/2
        print('Dien tich=',round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3),sep='')
    else:
        print('Khong hop le')