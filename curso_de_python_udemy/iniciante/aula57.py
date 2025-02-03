"""
lista de listas e seus indices
"""
salas = [
    ['maria', 'helena', ],
    ['elaine', ],
    ['luiz', 'joao', 'eduarda',],
]

# print(salas[2][3][2])

for sala in salas:
    print(f'a sala é {sala}')
    for aluno in sala:
        print(aluno)
