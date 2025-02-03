pizzas = ['4 cheese', 'chocolate', 'portuguese']
for pizza in pizzas[2:5]:
    print(f'i like {pizza} pizza')
print('eu gosto desses sabores pois são muito gostosos')

friend_pizzas = pizzas[:]
pizzas.append('rola')
friend_pizzas.append('cu')
for pizza in pizzas:
    print(f'my favorie pizzas are: {pizza}')
for pizza in friend_pizzas:
    print(f'my friends favorite pizzas are: {pizza}')