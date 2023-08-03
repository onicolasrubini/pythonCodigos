prod=str(input("Informe qual o produto? "))
qntd=int(input("Quantos comprou? "))
vuni=float(input("o Valor unitário é? "))
desc=float(input("Qual valor de desonto? "))
total=vuni+qntd
desconto=total*desc/100
totall=total-desconto
print(prod)
print("O total a pagar é R$",totall)