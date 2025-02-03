# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opções': ['1', '3', '4', '5'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opções': ['25', '55', '10', '51'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opções': ['4', '5', '2', '1'],
        'resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('pergunta: ', pergunta['pergunta'])
    print()
    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('acertou')
    else:
        print('errou')
    print()

print('voce acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas. ')