"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 49 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega
CONDIÇAO_RANGE = (local_carro == LOCAL_1 + 1) or (local_carro == LOCAL_1) or (local_carro == LOCAL_1 - 1)


if CONDIÇAO_RANGE:
    if velocidade >= RADAR_1:
        print("O carro ultrapassou o limite de velociade")
    else:
        print("tudo ok!")
else:
    print("O veículo não está no range do radar")