sal=float(input('Digite seu salário atual:'))
if sal < 500:
    t=sal*15
    print(sal,'\n15%','\nSeu novo salário será R$%.2f'%t)
elif sal >500 and sal <1000:
    t2=sal*10
    print(sal,'\n10%','\nSeu novo salário será R$%.2f'%t2)
else:
    t3=sal*5
    print(sal,'\n5%','\nSeu novo salário será R$%.2f'%t3)