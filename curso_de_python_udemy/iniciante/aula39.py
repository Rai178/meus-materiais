"""
iterando strings com while
"""

 # iteráveis

nome = 'luiz otávio'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1

print(novo_nome)