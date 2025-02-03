# exercicios com funcoes

"""
crie uma funcao que multiplica todos os argumentos
nao nomeados recebidos 
retorne o total para uma variavel e mostre o valor da variavel

crie uma funcao fala se um numero é par ou impar
retorne se o numero é par ou impar.
"""

def multiplica(*args):
    total = 1
    for numero in args:
        total = numero * total
    return total
    
num = multiplica(5, 3, 789865)
print(num)

def fala():
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
fala()
print(fala())