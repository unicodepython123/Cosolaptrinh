a=float(input("a="))
b=float(input('b='))
c=float(input('c='))
if(a>b):
    if(b>c):
        print('SLN='+str(a))
        print('SBN='+str(c))
    elif(a>c):
        print('SLN='+str(a))
        print('SBN='+str(b))
    else:
        print('SLN='+str(c))
        print('SBN='+str(b))
else:
    if(a>c):
        print('SLN='+str(b))
        print('SBN='+str(c))
    elif(b>c):
        print('SLN='+str(b))
        print('SBN='+str(a))
    else:
        print('SLN='+str(c))
        print('SBN='+str(a))
        
        