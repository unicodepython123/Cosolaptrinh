import math 
a=float(input())
b=float(input())
c=float(input())
if(a,b,c >0):
    if(a+b-c>0 and a+c-b>0 and c+b-a>0):
        if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
            print('Tam giac vuong')
        elif(a==b==c):
            print('Tam giac deu')
        else:
            print('Tam giac loai khac')
    else:
        print('Khong hop le')