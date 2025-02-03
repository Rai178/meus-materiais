# def soma_todos(*numeros):
#     resultado = 0
#     for numero in numeros:
#         resultado += numero
#     return resultado

# print(soma_todos(2,3))

# def imprimir_dados_pessoais(**keys):
#     for key, value in keys.items():
#         print(f'{key}: {value}')

# imprimir_dados_pessoais(nome='joão', idade=30, cidade='sao paulo')

# def calcular_media(nota1, nota2, nota3):
#     media = (nota1 + nota2 + nota3)/3
#     return media

# notas = [8, 7.5, 9]
# print(calcular_media(*notas))

# def info_completa(nome, *hobbies, idade=0, **kwargs):
#     print(f'nome: {nome}')
#     print(f'idade: {idade}')

#     hobbies_list = []
#     for hobbie in hobbies:
#         hobbies_list.append(hobbie)
        

#         print(f'hobbies: {", ".join(hobbies_list)}')

#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# info_completa('ana', 'leitura', 'caminhada', idade=25, cidade='rio de janeiro')

# def detalhes_compra(*items, **kwargs):
#     items_list = []
#     for item in items:
#         items_list.append(item)
    
#         print(f'Items comprados: {", ".join(items_list)}')

#     for key, value in kwargs.items():
#         print(f'detalhes: {key}: {value}')

# detalhes_compra('Camisa', 'Calça', 'Sapato', metodo_pagamento='Cartão', data='23/10/2024')

# def contar_palavras(texto):
#     """conta a frequencia de cada palavra em um texto."""
#     contagem = {}
#     for palavra in texto.split():
#         contagem[palavra] = contagem.get(palavra, 0) + 1
#     return contagem

# texto = 'vai tomar no olho do seu cu'
# resultado = contar_palavras(texto)
# print(resultado)

# def criar_perfil(nome, idade, cidade=None, profissao=None):
#     perfil = {
#         'nome': nome,
#         'idade': idade
#     }
#     if cidade:
#         perfil['cidade'] = cidade
#     if profissao:
#         perfil['profissao'] = profissao
#     return perfil

# perfil_usuario = criar_perfil('ana', 30, cidade='sao paulo')
# print(perfil_usuario.get('profissao', 'informacao nao fornecida'))

# def exibir_endereco(rua, numero, cidade):
#     return f'{endereco}'

# endereco = {'rua': 'av. paulista', 'numero': 1000, 'cidade': 'sao paulo'}

# exibir_endereco(**endereco)

# # desempacotando uma lista
# frutas = ['maca', 'banana', 'laranja']
# fruta1, fruta2, fruta3 = frutas
# print(fruta1)
# print(fruta2)
# print(fruta3)

# # desempacotando uma tupla
# coordenadas = (3, 4)
# x, y = coordenadas
# print(x) 
# print(y)

# numeros = [1, 2, 3, 4, 5]
# primeiro, *restante = numeros
# print(primeiro)
# print(restante)

# def somar(x, y, z):
#     return x + y + z

# numeros = [1, 2, 3]
# resultado = somar(*numeros)
# print(resultado)

# def criar_usuario(nome, idade, cidade):
#     usuario = {'nome': nome, 'idade': idade, 'cidade': cidade}
#     return usuario

# dados_usuario = {'nome': 'joao', 'idade': 30, 'cidade': 'sao paulo'}
# usuario = criar_usuario(**dados_usuario)
# print(usuario)

# def calcular_media(*numeros):
#     return sum(numeros) / len(numeros)

# notas = [8, 7, 9, 10]
# media = calcular_media(*notas)
# print(media)

# argumentos posicionais:
def soma(*numeros):
    return sum(numeros)

resultado = soma(1, 2, 3, 4, 5)

# argumentos nomeados:
def criar_usuario(**kwargs):
    return kwargs

usuario = criar_usuario(nome='joao', idade=30, cidade='sao paulo')

# combinando desempacotamento com listas e dicionarios:
def criar_produto(nome, preco, *ingredientes, **informacoes_adicionais):
    produto = {'nome': nome, 'preco': preco, 'igredientes': ingredientes, 'informacoes_adicionais': informacoes_adicionais}
    return produto

ingredientes = ['farinha', 'ovo', 'leite']
informacoes = {'marca': 'X', 'validade': '15/09/2024'}
produto = criar_produto('bolo', 15, *ingredientes, **informacoes)

#desempacotando iteratores:
def processar_dados(*iteravel):
    for item in iteravel:
        #processar cada item
        print(item)

dados = [(1, 2), (3, 4), (5, 6)]
processar_dados(*dados) # desempacota cada tupla e passa como argumento individual

# desempacotando conjuntos:
def encontrar_intersecao(conjunto1, conjunto2):
    return conjunto1 & conjunto2

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
intersecao = encontrar_intersecao(*[conjunto_a, conjunto_b])

# desempacotamento em expressoes geradoras:
pares = [(1, 2), (3, 4), (5, 6)]
novos_pares = [(x*2, y*2) for x, y in pares]

# desempacotamento em compreenssoes de dicionarios
dicionario = {'a': 1, 'b': 2}
novo_dicionario = {k*2: v*2 for k, v in dicionario.items()}
