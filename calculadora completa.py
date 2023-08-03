print('-'*50)
print('                  Calculadora')
print('-'*50)

while True:
    print('Digite...')
    print('(M) Multplicação | (D) Divisão | (A) Adição | (S) Subtração | (V) Volume do Cubo |(E) Exponenciação\n(R) Raiz Quadrada | (Q) Área do Quadrado | (ME) Média de 4 Notas | (F) Fatorial | (0) Sair')
    a=input('\nEscolha o que deseja fazer:')
    print('='*36)

    cal=a.upper()
    cal=='M' or cal=='D' or cal=='A' or cal=='S' or cal=='V' or cal=='E' or cal=='R' or cal=='Q' or cal=='ME' or cal=='F' or cal=='0'

    if cal=='M':
        print('--- Bem vindo a Multiplicação ---')
        nm1=int(input('Digite um número:'))
        nm2=int(input('Digite outro número:'))
        mult=nm1*nm2
        print(nm1,'x',nm2,'=',mult)
        print('='*36)

    elif cal=='D':
        print('--- Bem vindo a Divisão ---')
        nm1=float(input('Digite um número:'))
        nm2=float(input('Digite outro número:'))
        div=nm1/nm2
        print(nm1,'/',nm2,'=',div)
        print('='*36)

    elif cal=='A':
        print('--- Bem vindo a Adição ---')
        nm1=int(input('Digite um número:'))
        nm2=int(input('Digite outro número:'))
        soma=nm1+nm2
        print(nm1,'+',nm2,'=',soma)
        print('='*36)

    elif cal=='S':
        print('--- Bem vindo a Subtração ---')
        nm1=float(input('Digite um número:'))
        nm2=float(input('Digite outro número:'))
        sub=nm1+nm2
        print(nm1,'-',nm2,'=',sub)
        print('='*36)

    elif cal=='V':
        print('--- Bem vindo a Volume do Cubo ---')
        nm1=float(input('Digite a área do cubo:'))
        vol=nm1**3
        print('O volume do cubo é',vol)
        print('='*36)

    elif cal=='E':
        print('--- Bem vindo a Exponenciação ---')
        nm1=int(input('Digite um número:'))
        nm2=int(input('Digite o número da exponenciação:'))
        exp=nm1**nm2
        print('O valor da exponenciação é',exp)
        print('='*36)

    elif cal=='R':
        print('--- Bem vindo a Raiz Quadrada ---')
        nm1=float(input('Digite um número:'))
        raiz=nm1**(1/2)
        print('O valor da raiz quadrada é',raiz)
        print('='*36)

    elif cal=='Q':
        print('--- Bem vindo a Área do Quadrado ---')
        nm1=float(input('Digite um número:'))
        area=nm1*nm1
        print(nm1,'x',nm1,'=',area)
        print('='*36)

    elif cal=='ME':
        print('--- Bem vindo a Média ---')
        nm1=float(input('Digite sua 1a Nota:'))
        nm2=float(input('Digite sua 2a Nota:'))
        nm3=float(input('Digite sua 3a Nota:'))
        nm4=float(input('Digite sua 4a Nota:'))
        media= (nm1+nm2+nm3+nm4) / 4
        print('Sua média é',media)
        print('='*36)

    elif cal=='F':
       cont=1
       resul=1
       print('--- Bem vindo a Fatorial ---')
       nm=int(input('Digite um número:'))
       while cont <= nm:
           resul *= cont
           cont += 1
           print(resul)
       print('='*36)

    elif cal == '0':
        print('Obrigado por usar nossa calculadora!\nSaindo...')
        break

    else:
        print('Inválido\nDigite novamente')
        print('='*36)