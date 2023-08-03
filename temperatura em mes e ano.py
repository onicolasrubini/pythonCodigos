lista_celsius=[]
anos=[]
meses=[]
cont=0
while True:
    celsius=input('informe a temperatura em Celcius:')
    if celsius == 'x':
        break
    if celsius.isnumeric() == True:  # isnumeric é para ver se é um número
        celsius = int(celsius)
        lista_celsius.append(celsius)
        mes=0
        while mes < 1 or mes > 12:
            mes=int(input('Em qual mês estamos?'))
            meses.append(mes)
            ano=int(input('Em que ano estamos?'))
            anos.append(ano)
    cont += 1

if lista_celsius == []:
    print('Encerrado')
else:
    omaior = max(lista_celsius)
    omenor = min(lista_celsius)
    maior = lista_celsius.index(omaior)  # index olha o índice de uma lista
    menor = lista_celsius.index(omenor)
    mesmaior = meses[maior]
    mesmenor = meses[menor]
    anomaior = anos[maior]
    anomenor = anos[menor]
    soma = sum(lista_celsius)
    total = soma / cont

print('A média das temperaturas é',total)
print('A temperatura máxima é',max(lista_celsius),'Celsius em',mesmaior,'/',anomaior)
print('A menor temperatura é',min(lista_celsius),'Celsius em',mesmenor,'/',anomenor)