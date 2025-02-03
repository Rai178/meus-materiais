"""
introdução as funcoes (def) em python
funçoes são trechos de código usados para 
replicar determinada acao ao longo do seu código
elas podem receber valores para parametros (argumentos) 
e retornar um valor especifico
por padrao, funcoes python retornam None (nada).
"""
# def Print(a, b, c):
#     print('varias')
#     print('varias2')
#     print('varias3')
#     print('varias4')


# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome= 'sem nome'):
    print(f'ola, {nome}')

saudacao('luiz')
saudacao('cu')
saudacao()