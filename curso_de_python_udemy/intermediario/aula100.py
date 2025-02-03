import copy
# exercicios
# aumente os precos dos produtos a seguir em 10%
# gere novos_produtos por deep copy (copia profunda)
produtos = [
    {'nome': 'produto 1', 'preco': 10.00},
    {'nome': 'produto 2', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 4', 'preco': 105.87},
    {'nome': 'produto 5', 'preco': 69.90},
]

# ordene os produtos por nome decrescente (do maior para o menor)
# gere produtos_ordenados_por_nome por deep copy (copia profunda)

# ordene os produtos por preco crescente (do menor para maior)
# gere produtos_ordenados_por_preco por deep copy (copia profunda)



for produto in produtos:
    produto['preco'] *= 1.10

novos_produtos = copy.deepcopy(produtos)

produtos_ordenados = sorted(produtos, key=lambda x: x['nome'], reverse=True)
produtos_ordenados_por_nome = copy.deepcopy(produtos_ordenados)

produtos_ordenados_p = sorted(produtos, key=lambda p: p['preco'], reverse=False)
produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_p)

print(novos_produtos)
print(produtos_ordenados_por_nome)
print(produtos_ordenados_por_preco)




