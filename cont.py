class Cont():


    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.__saldo = 0
        self.__cpf = cpf
        self.__senha = senha


    def extrato(self,senha):

        if self.__senha != senha:
            print('X| Senha Inválida |X')
        else:
            print('R$',self.__saldo)


    def sacar(self,saque,senha):
        if self.__senha == senha:

            if self.__saldo <= saque:
                print('X| Não tem dinheiro suficiente na sua conta |X')   
            else:
                self.__saldo = self.__saldo - saque

        else:
            print('X| Senha Inválida |X')
            
           
    def depositar(self,deposito):
        self.__saldo = self.__saldo + deposito