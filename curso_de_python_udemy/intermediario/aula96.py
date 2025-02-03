"""
modulos padrao do python (import, from, as e *)
inteiro - import nome_modulo
vantagens: voce tem o namespace do modulo
desvantagens: nomes grandes

partes - from nome_modulo import objeto1, objeto2
vantagens: nomes pequenos
desvantagens: sem o namespace do modulo

alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import objeto as apelido
vantagens: voce pode reservar nomes para seu codigo
desvantagens: pode ficar fora do padrao da linguagem

ma pratica - from nome_modulo import *
vantagens: importa tudo de um modulo
desvantagens: importa tudo de um modulo 
"""

# import sys

# platform = 'a minha'
# print(sys.platform)
# print(platform)

# from sys import exit, platform

# print(platform)

# import sys as s
# sys = 'alguma coida'
# print(s.platform)
# print(sys)

# from sys import exit as ex
# from sys import platform as pf

# print(pf )

from sys import *

print(platform)
exit()