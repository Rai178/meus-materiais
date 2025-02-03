"""
exercicio - unir listas
crie uma funcao zipper (como o zipper de roupas)
o trabalho dessa funcao sera unir duas listas na ordem 
use todos os valores da menor lista.

"""
from itertools import zip_longest

# def zipper(L1, L2):
#     intervalo = min(len(L1), len(L2))
#     return [(L1[i], L2[i]) for i in range(intervalo)]

l1 = ['salvador', 'ubatuba', 'belo horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))