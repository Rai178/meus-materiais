"""
funcao lambda em python 
a funcao lambda é uma funcao como qualquer outra em python. porém, são funcoes anonimas
que contem apenas uma linha. ou seja, tudo deve ser contido dentro de uma unica expressão.
"""
# lista = [3, 4, 6, 7, 8, 4, 3, 2, 5, ]
# lista.sort(reverse=True)
#sorted(lista)

lista = [
    {'nome': 'luiz', 'sobrenome': 'miranda'},
    {'nome': 'maria', 'sobrenome': 'oliveira'},
    {'nome': 'daniel', 'sobrenome': 'silva'},
    {'nome': 'eduardo', 'sobrenome': 'moreira'},
    {'nome': 'aline', 'sobrenome': 'souza'},
]

def exibir(dicionario):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

