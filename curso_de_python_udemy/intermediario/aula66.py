"""
argumentos nomeados e não nomeado em funcoes python
argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # definição
    print(f'{x=} + y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(y=2, z=3, x=1)

print(1, 2, 3, sep='-')