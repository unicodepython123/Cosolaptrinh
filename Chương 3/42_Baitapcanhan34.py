toan=float(input())
ly=float(input())
hoa=float(input())
ĐTB=(toan*2+ly*3+hoa*1)/6
if(ĐTB<3):
    print('Kem')
elif(ĐTB<=3<5):
    print('Yeu')
elif(5<=ĐTB<=6):
    print('Trung binh')
elif(6<=ĐTB<7):
    print('Trung binh Kha')
elif(7<=ĐTB<8):
    print('Kha')
elif(8<=ĐTB<9):
    print('Gioi')
else:
    print('Xuat sac')
    