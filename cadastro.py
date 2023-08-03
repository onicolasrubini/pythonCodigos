lista_nome=[]
lista_sobrenome=[]
lista_endereco=[]
lista_bairro=[]
lista_city=[]
lista_estado=[]
lista_pais=[]
lista_fone=[]
lista_cpf=[]
lista_peso=[]
lista_alt=[]
lista_idade=[]
lista_n_cartao=[]
lista_email=[]
lista_cep=[]
lista_nt1=[]
lista_nt2=[]
lista_nt3=[]
lista_nt4=[]
lista_media=[]
lista_serie=[]
lista_classe=[]
lista_sx=[]
lista_cor=[]
lista_matricula=[]
cont=0

while True:
    comecar=input('\n> Para Começar, digite 1\n> Para Consultar, digite 2\n> Para Excluir, digite 3\n> Para Finalizar, digite 0\n')
    if comecar == '1':
        nome=input('Digite seu nome:')
        nome=nome.capitalize()
        sobrenome=input('Digite seu sobrenome:')
        sobrenome=sobrenome.capitalize()
        endereco=input('Informe seu endereço(Rua, n):')
        bairro=input('Informe seu bairro:')
        cidade=input('Informe a cidade que mora:')
        cidade=cidade.capitalize()
        estado=input('Informe seu estado:')
        estado=estado.capitalize()
        pais=input('Informe seu país:')
        pais=pais.capitalize()
        fone=int(input('Informe seu telefone:'))
        cpf=int(input('Informe seu CPF:'))
        peso=float(input('Qual seu peso?'))
        alt=float(input('Qual sua altura?'))
        idade=int(input('Quantos anos você tem?'))
        n_cartao=int(input('Informe o número do seu cartão:'))
        email=input('Informe seu email:')
        cep=int(input('Informe seu CEP:'))
        nt1=float(input('Informe sua 1a nota:'))
        nt2=float(input('Informe sua 2a nota:'))
        nt3=float(input('Informe sua 3a nota:'))
        nt4=float(input('Informe sua 4a nota:'))
        media=(nt1+nt2+nt3+nt4) / 4
        serie=int(input('Informe sua série:'))
        classe=input('Informe sua classe:')
        sx=input('Informe seu sexo:')
        cor=input('Informe sua cor:')

        lista_nome.append(nome)
        lista_sobrenome.append(sobrenome)
        lista_endereco.append(endereco)
        lista_bairro.append(bairro)
        lista_city.append(cidade)
        lista_estado.append(estado)
        lista_pais.append(pais)
        lista_fone.append(fone)
        lista_cpf.append(cpf)
        lista_peso.append(peso)
        lista_alt.append(alt)
        lista_idade.append(idade)
        lista_n_cartao.append(n_cartao)
        lista_email.append(email)
        lista_cep.append(cep)
        lista_nt1.append(nt1)
        lista_nt2.append(nt2)
        lista_nt3.append(nt3)
        lista_nt4.append(nt4)
        lista_media.append(media)
        lista_serie.append(serie)
        lista_classe.append(classe)
        lista_sx.append(sx)
        lista_cor.append(cor)

        cont +=1
        lista_matricula.append(cont)

        print(lista_nome)
        print(lista_sobrenome)
        print(lista_endereco)
        print(lista_bairro)
        print(lista_city)
        print(lista_estado)
        print(lista_pais)
        print(lista_fone)
        print(lista_cpf)
        print(lista_peso)
        print(lista_alt)
        print(lista_idade)
        print(lista_n_cartao)
        print(lista_email)
        print(lista_cep)
        print(lista_nt1)
        print(lista_nt2)
        print(lista_nt3)
        print(lista_nt4)
        print(lista_media)
        print(lista_serie)
        print(lista_classe)
        print(lista_sx)
        print(lista_cor)
        print(lista_matricula)
        print('> Sua matrícula é a',cont)

    elif comecar == "2":
        matricula=int(input('> Digite a matrícula que deseja ver:'))
        print('Nome:',lista_nome[matricula-1])
        print('Sobrenome:',lista_sobrenome[matricula-1])
        print('Endereço:',lista_endereco[matricula-1])
        print('Bairro:',lista_bairro[matricula-1])
        print('Cidade:',lista_city[matricula-1])
        print('Estado:',lista_estado[matricula-1])
        print('País:',lista_pais[matricula-1])
        print('Telefone:',lista_fone[matricula-1])
        print('CPF:',lista_cpf[matricula-1])
        print('Peso:',lista_peso[matricula-1])
        print('Altura:',lista_alt[matricula-1])
        print('Idade:',lista_idade[matricula-1])
        print('Número do cartão:',lista_n_cartao[matricula-1])
        print('E-mail:',lista_email[matricula-1])
        print('CEP:',lista_cep[matricula-1])
        print('Nota 1:',lista_nt1[matricula-1])
        print('Nota 2:',lista_nt2[matricula-1])
        print('Nota 3:',lista_nt3[matricula-1])
        print('Nota 4:',lista_nt4[matricula-1])
        print('Média:',lista_media[matricula-1])
        print('Série:',lista_serie[matricula-1])
        print('Classe:',lista_classe[matricula-1])
        print('Sexo:',lista_sx[matricula-1])
        print('Cor:',lista_cor[matricula-1])
        print('Matrícula:',lista_matricula[matricula-1])

    elif comecar == '0':
        break

    elif comecar == '3':
        delete=int(input('> Digite a matrícula a ser excluída:'))
        del(lista_nome[delete-1])
        del(lista_sobrenome[delete-1])
        del(lista_endereco[delete-1])
        del(lista_bairro[delete-1])
        del(lista_city[delete-1])
        del(lista_estado[delete-1])
        del(lista_pais[delete-1])
        del(lista_fone[delete-1])
        del(lista_cpf[delete-1])
        del(lista_peso[delete-1])
        del(lista_alt[delete-1])
        del(lista_idade[delete-1])
        del(lista_n_cartao[delete-1])
        del(lista_email[delete-1])
        del(lista_cep[delete-1])
        del(lista_nt1[delete-1])
        del(lista_nt2[delete-1])
        del(lista_nt3[delete-1])
        del(lista_nt4[delete-1])
        del(lista_media[delete-1])
        del(lista_serie[delete-1])
        del(lista_classe[delete-1])
        del(lista_sx[delete-1])
        del(lista_cor[delete-1])
        del(lista_matricula[delete-1])
        print('Matrícula excluida com sucesso!')

    else:
        print('X Inválido, Tente Novamente...')