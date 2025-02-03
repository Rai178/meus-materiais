"""
Exercício
peça ao usuário para digitar seu nome 
peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "desculpe, você deixou campos vazios."
"""

nome_usuario = input("Seu nome é? ")
idade_usuario = input("Qual é sua idade? ")
nome_usuario_invertido = nome_usuario[::-1]

if nome_usuario and idade_usuario:
    print(f"Seu nome é {nome_usuario}")
    print(f"Seu nome invertido é {nome_usuario_invertido}")
    if ' ' in nome_usuario:
        print("O nome contém espaços")
    else:
        print("O nome não contém espaços.")
    print(f'"{nome_usuario[1]}" é a primeira letra de seu nome.')
    print(f'"{nome_usuario[-1]}" é a ultima letra do seu nome.')
else:
    print("você deixou campos vazios.")
