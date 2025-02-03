# desempacotamento em chamadas
# de metodos e funcoes
# string = 'ABCD'
# lista = ['maria', 'helena', 1, 2, 3, 'eduarda']
# tupla = 'python', 'é', 'legal'
salas = [
    ['maria', 'helena', ],
    ['elaine', ],
    ['luiz', 'joao', 'eduarda',],
]

# # p, b, *_, ap, u = lista
# # print(p, u, ap)

# print('maria', 'helena', 1, 2, 3, 'eduarda')
# print(*lista) 
# print(*string)
# print(*tupla)

print(*salas, sep='\n')