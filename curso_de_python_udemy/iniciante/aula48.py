"""
listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete

"""
#        +01234
# #        -54321
# string = 'ABCDE' # 5 caracteres (len)

# # print(bool(lista))  # falsy
# # print(lista, type(lista))

# lista = [123, True, 'Luiz Otávio', 1.2, []] 
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# lista.pop()
# print(lista)

# lista.append('Luiz')
# nome = lista.pop()
# lista.append(123)
del lista[-1]
# lista.insert(0, 5)
# print(lista)


# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)
# print(lista_d)

"""
cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
lista_a = ['luiz', 'maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)