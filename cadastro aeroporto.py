import os
listaCliente=[]
listaPassagem=[]
listaAviao=[]
listaTripulacao=[]
print('\n---- Bem vindo a PontoCom Passagens ----')
while True:
    menu=input('\nDigite.:\n1 - Cadastrar\n2 - Imprimir Relatório\n0 - Sair\n> ')
    if menu == '1':
        cadastro=input('1 - Cadastro do Cliente\n2 - Cadastro da Passagem\n3 - Cadastro do Avião\n4 - Cadastro da Tripulação\n0 - Sair\n> ')
        if cadastro == '1':
            while True:
                try:
                    print('\nFaça seu cadastro aqui')
                    nome=input('Nome: ')
                    sobrenome=input('Sobrenome: ')
                    listaCliente.append(nome.capitalize())
                    listaCliente.append(sobrenome.capitalize())
                    rg=int(input('Informe seu Rg: '))
                    cpf=int(input('Informe seu CPF:'))
                    endereco=input('Informe seu Endereço: ')
                    fone=input('Número de Telefone: ')
                    idade=int(input('Informe sua Idade: '))
                    listaCliente.append(rg)
                    listaCliente.append(cpf)
                    listaCliente.append(endereco)
                    listaCliente.append(fone)
                    listaCliente.append(idade)
                except TypeError:
                    print('\nX [Não é possivel números com letras]\n')
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print('\nX [Digite apenas números]\n')
                    os.system("pause")
                    os.system("cls")
                except:
                    print('\nX [Erro Desconhecido]\n')
                    os.system("pause")
                    os.system("cls")
                else:
                    break
        elif cadastro == '2':
            while True:
                try:
                    print('Faça o Cadastro da Passagem aqui')
                    destino=input('Qual seu Destino: ')
                    origem=input('Informe de onde sairá: ')
                    duracao=input('Informe a Duração da viagem: ')
                    listaPassagem.append(destino.capitalize())
                    listaPassagem.append(origem.capitalize())
                    listaPassagem.append(duracao)
                    valor=float(input('Informe o preço da Passagem: '))
                    desc=valor *5 /100
                    desconto= valor - desc
                    listaPassagem.append(valor)
                    listaPassagem.append(desconto)
                except ZeroDivisionError:
                    print('\nX [É impossivel dividir por zero]\n')
                    os.system("pause")
                    os.system("cls")
                except TypeError:
                    print('\nX [Não é possivel números com letras]\n')
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print('\nX [Digite apenas números]\n')
                    os.system("pause")
                    os.system("cls")
                except:
                    print('\nX [Erro Desconhecido]\n')
                    os.system("pause")
                    os.system("cls")
                else:
                    break
        elif cadastro == '3':
            while True:
                try:
                    print('Faça o Cadastro do Avião aqui')
                    modelo=input('Modelo do avião: ')
                    ano=('Ano do avião: ')
                    horasVoo=input('Quantas horas voo tem o avião: ')
                    cor=input('Cor do avião: ')
                    passageiros=int(input('Quantos passageiros no avião: '))
                    listaAviao.append(modelo)
                    listaAviao.append(ano)
                    listaAviao.append(horasVoo)
                    listaAviao.append(cor)
                    listaAviao.append(passageiros)
                except TypeError:
                    print('\nX [Não é possivel números com letras]\n')
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print('\nX [Digite apenas números]\n')
                    os.system("pause")
                    os.system("cls")
                except:
                    print('\nX [Erro Desconhecido]\n')
                    os.system("pause")
                    os.system("cls")
                else:
                    break
        elif cadastro == '4':
            while True:
                try:
                    print('Faça o Cadastro da Tripulação aqui')
                    nomeTrip=input('Nome: ')
                    cargo=('Descreva seu cargo: ')
                    idadeTrip=int(input('Informe sua Idade: '))
                    admissao=input('Digite sua Admissão: ')
                    foneTrip=input('Número de Telefone: ')
                    listaTripulacao.append(nomeTrip.capitalize())
                    listaTripulacao.append(cargo)
                    listaTripulacao.append(idadeTrip)
                    listaTripulacao.append(admissao)
                    listaTripulacao.append(foneTrip)
                except TypeError:
                    print('\nX [Não é possivel números com letras]\n')
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print('\nX [Digite apenas números]\n')
                    os.system("pause")
                    os.system("cls")
                except:
                    print('\nX [Erro Desconhecido]\n')
                    os.system("pause")
                    os.system("cls")
                else:
                    break
        elif cadastro == '0':
            break
        else:
            print('\nX [Função Inválida]\n')
    elif menu == '2':
        for relatorio in listaCliente:
            print('Relatório do Cliente:\n',relatorio)    
        for relatorio in listaPassagem:
            print('Relatório da Passagem:\n',relatorio)
        for relatorio in listaAviao:
            print('Relatório do Avião:\n',relatorio)
        for relatorio in listaTripulacao:
            print('Relatório da Tripulação:\n',relatorio)
        if listaCliente == [] and listaPassagem == [] and listaAviao == [] and listaTripulacao == []:
            print('[Relatório vazio]')
    elif menu == '0':
        break
    else:
        print('\nX [Função Inválida]\n')