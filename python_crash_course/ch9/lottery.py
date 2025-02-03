import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 's', 'd', 'f', 'c']
resultados = [] 
my_ticket = [4, 9, 3, 4]

for _ in range(4):
    item = random.choice(list)
    resultados.append(item)

while True:
    resultados = []

    for _ in range(4):
        item = random.choice(list)
        resultados.append(item)
    
    if resultados == my_ticket:
        print("Você venceu a loteria")
        break

    print("Números gerados:", resultados)
   