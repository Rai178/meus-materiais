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
import copy



d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()
#copia rasa

d2['c1'] = 100
d2['l1'][1] = 999999
print(d1)
print(d2)