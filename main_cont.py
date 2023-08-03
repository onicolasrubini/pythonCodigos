from cont import *
import os

while True:
    menu = input('[1] Cadastro | [2] Saldo | [3] Saque | [4] Depósito | [0] Voltar\n> ')
    os.system("cls")

    if menu == '1':

        try:
            print('Realizar cadastro')
            nome = input('Digite seu Nome: ')
            cpf = int(input('Informe seu CPF: '))
            senha = input('Digite sua senha:')
            conta = Cont(nome,cpf,senha)
            os.system("cls")


        except:
            print('X| Erro |X')
            os.system("pause")
            os.system("cls")


    elif menu == '2':
        senha_extrato = input('Confirme sua senha para ver o saldo:\n')
        os.system("cls")
        conta.extrato(senha_extrato)
        os.system("pause")
        os.system("cls")


    elif menu == '3':
        try:
            senha_saque = input('Confirme sua senha para sacar:\n')
            os.system("cls")
            saque_din = int(input('Quantos deseja sacar:\nR$'))
            conta.sacar(saque_din,senha_saque)
            os.system("pause")
            os.system("cls")


        except:
            print('X| Erro |X')
            os.system("pause")
            os.system("cls")


    elif menu == '4':
        try:
            depositar_din = float(input('Quantos deseja depositar:\nR$'))
            conta.depositar(depositar_din)
            os.system("cls")


        except:
            print('X| digite apenas números |X')
            os.system("pause")
            os.system("cls")


    elif menu == '0':
        break


    else:
        print('X| Digite um dos valores acima |X')
        os.system("pause")
        os.system("cls")