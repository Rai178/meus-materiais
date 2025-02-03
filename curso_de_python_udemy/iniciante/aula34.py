"""
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
"""
condição = True

while condição:
    nome = input('qual o seu nome: ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break

print('acabou')