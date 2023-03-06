SoKW=float(input('Tieu thu: '))
if(SoKW>=201):
    print('Phai tra=',550*100+750*50+950*50+1350*(SoKW-200)+0,1*(550*100+750*50+950*50+1350*(SoKW-200)),sep='')
elif(151<=SoKW<=200):
    print('Phai tra=',(550*100+750*50+950*(SoKW-150))+0.1*(550*100+750*50+950*(SoKW-150)),sep='')
elif(101<=SoKW<=150):
    print('Phai tra=',(550*100+750*(SoKW-100))+0.1*(550*100+750*(SoKW-100)))
elif(1<=SoKW<=100):
    print('Phai tra=',550*SoKW+0.1*(550*SoKW),sep='')