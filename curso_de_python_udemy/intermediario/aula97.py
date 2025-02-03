"""
entendendo os seus propios modulos python
o primeiro modulo executado chama-se __main__
voce pode importar outro modulo inteiro ou parte do modulo
o python conhece a pasta onde o __main__ está e as pastas abaixo dele.
ele nao reconhece pastas e modulos aceima do __main__ por padrao
o python conhece todos os modulos e pacotes presentes nos caminhos de sys.path

"""

import aula97_m
from aula97_m import soma, variavel_modulo


print("este modulo se chama", __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))

