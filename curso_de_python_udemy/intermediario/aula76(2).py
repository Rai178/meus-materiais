"""
metodos uteis dos dicionario em python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
setdefalt - adiciona valor se a chave não existe
"""
pessoa = {
    'nome': 'luiz otavio',
    'sobrenome': 'miranda 3',
    # 'idade': 900
}

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

for valor in pessoa.values():
    print(valor)

# for chave, valor in pessoa.items():
    # print(chave, valor)

