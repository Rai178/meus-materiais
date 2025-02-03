# groupby - agrupando valores (itertools)
from itertools import groupby


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'leticia', 'nota': 'B'},
    {'nome': 'fabricio', 'nota': 'A'},
    {'nome': 'rosemary', 'nota': 'C'},
    {'nome': 'joana', 'nota': 'D'},
    {'nome': 'joao', 'nota': 'A'},
    {'nome': 'eduardo', 'nota': 'B'},
    {'nome': 'andre', 'nota': 'A'},
    {'nome': 'anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)


for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

