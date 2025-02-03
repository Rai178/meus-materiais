"""
sets - conjuntos em python (tipo set)
conjuntos são ensinados na matematica
representados graficamente pelo diagrama de venn
sets em python sao mutaveis, porem aceitam apenas tipos imutaveis 
como valor interno.

criando um set
set(iteravel) ou {1, 2, 3}

sets sao eficientes para remover valores duplicados 
de iteraveis.
- seus valores serao sempre unicos;
- eles não tem indexes;
- eles não garantem ordem;
- eles são iteraveis (for, in, not in)

metodos uteis:
add, update, clear, discard

operadores uteis:
uniao | uniao (union) - une
intersecção & (intersection) - itens presentes em ambos
diferença - items presentes apenas no set da esquerda
"""

# s1 = set('luiz')
# s1 = {'luiz', 1, 2, 3}
# s1 = set() # vazio
# s1 = {'luiz', 1, 2, 3} # com dados
# s1 = {1, 2, 3, 3, 3, 3, 3, 3, 1}
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)

# s1 = s1 = {1, 2, 3}
# print(3 in s1)
# for numero in s1:
#     print(numero)

s1 = set()
s1.add('luiz')
s1.add(1)
s1.update(('ola mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('ola mundo')
s1.discard('luiz')
print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)


