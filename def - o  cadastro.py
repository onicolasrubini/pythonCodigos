def cadastro():
    name = input('Qual seu nome:')
    age = int(input('Qual sua idade:'))
    return name,age  
    
print('Iniciando cadastro...')
nome,idade = cadastro()
print('Cadastro realizado com sucesso!')
print('Seu nome é',nome,'\nSua idade é',idade,'anos')