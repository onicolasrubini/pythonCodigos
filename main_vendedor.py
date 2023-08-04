from vendedor import * 
nomeVendedor=input("Digite o nome do vendedor:")
vendasMes=int(input("Digite quantas vendas %s fez no mês:"%nomeVendedor))

vendedor1 = Vendedor(nomeVendedor,vendasMes)
print(vendedor1.nome,end=' ')

vendedor1.bateu_meta(100)
print(vendedor1)