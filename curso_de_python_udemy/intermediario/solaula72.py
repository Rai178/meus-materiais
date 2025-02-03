
"""
crie uma funcao que multiplica todos os argumentos
nao nomeados recebidos 
retorne o total para uma variavel e mostre o valor da variavel

crie uma funcao fala se um numero é par ou impar
retorne se o numero é par ou impar.
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        toal *= numero
    return total

multicacao = multiplicar(1, 2, 3, 4, 5)
print(multicacao)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return 'par'
    return 'impar'
    
print(par_impar(2))