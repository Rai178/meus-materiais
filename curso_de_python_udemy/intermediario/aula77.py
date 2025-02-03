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
contador = 0

# resposta = input(perguntas[0]['pergunta'])
question1 = perguntas[0]['pergunta']
option1 = perguntas[0]['opções']
answer1 = perguntas[0]['resposta']

question2 = perguntas[1]['pergunta']
option2 = perguntas[1]['opções']
answer2 = perguntas[1]['resposta']

question3 = perguntas[2]['pergunta']
option3 = perguntas[2]['opções']
answer3 = perguntas[2]['resposta']


print(question1)
print()
print('opções:')
for indice, value in enumerate(option1, start=1):
    print(f'{indice}) {value}')

resp = input("escolha uma opcao: ")
if resp == '3':
    print('acertou')
    contador += 1
else:
    print('errou')

print(question2)
print()
print('opções:')
for indice, value in enumerate(option2, start=1):
    print(f'{indice}) {value}')

resp1 = input("escolha uma opcao: ")
if resp1 == '1':
    print('acertou')
    contador += 1
else:
    print('errou')

print(question3)
print()
print('opções:')
for indice, value in enumerate(option3, start=1):
    print(f'{indice}) {value}')

resp2 = input("escolha uma opcao: ")
if resp2 == '2':
    print('acertou')
    contador += 1
else:
    print('errou')

print(f'voce acertou {contador} de 3.')

    



    