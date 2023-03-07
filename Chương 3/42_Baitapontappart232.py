while True:
    n=int(input('Nhap so n='))
    if(1<=n<=50):
        j=1
        while (j<=n):
            print(j, end=' ')
            if(j%10==0):
                if(j+1<n):
                    print('')
            j=j+1     
        print('')
        break
    else:
        print('Hay nhap lai n')
    
         