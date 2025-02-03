lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [2, 4, 6, 8]

def soma(lista_a, lista_b):
    lista = list(zip(lista_a, lista_b))
    somas = [a + b for a, b in lista]
    return somas

print(soma(lista_a, lista_b))
