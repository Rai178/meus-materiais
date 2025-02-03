"""
exercicio - unir listas
crie uma funcao zipper (como o zipper de roupas)
o trabalho dessa funcao sera unir duas
listas na ordem.
use todos os valores da menor lista.
ex.:
"""
# ['salvador', 'ubatuba', 'belo horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# resultado
# [('salvador', 'BA'), ('ubatuba', 'SP'), ('belo horizonte', 'MG')]

def zip():
    list1 = ['salvador', 'ubatuba', 'belo horizonte']
    list2 = ['BA', 'SP', 'MG', 'RJ']

    lista_de_tuplas = []
    for i in range(len(list1)):
        lista_de_tuplas.append((list1[i], list2[i]))

    print(lista_de_tuplas)