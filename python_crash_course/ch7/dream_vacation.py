respostas = {}

pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("qual é o seu nome?")
    resposta = input("em qual lugar do mundo você gostaria de visitar um dia?")
    respostas[nome] = resposta

    repetir = input("Alguem mais irá fazer a pesquisa?")
    if repetir == 'não':
        pesquisa_ativa = False

    print("\nResultado da pesquisa")
    for nome, resposta in respostas.items():
        print(f"{nome} gostaria de viajar para {resposta}")