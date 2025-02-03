"""
interpolação basica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total é RS%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1534500, 1534500))