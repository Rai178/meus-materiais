# manipulando chaves e valores em dicionarios
pessoa = {}

##
##
chave = 'nome'

pessoa[chave] = 'luiz otavio'
pessoa['sobrenome'] = 'miranda'

print(pessoa[chave])

pessoa[chave] = 'maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('nao existe')
else:
    print(pessoa['sobrenome'])
# print('isso não vai')


#crud creat read update delete