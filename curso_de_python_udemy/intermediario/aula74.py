"""
closure e funcoes que retornam outras funcoes
"""
def criar_saudacao(saudacao):
    def sauda(nome):
         return f'{saudacao} , {nome}!'
    return sauda

falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao('boa noite')

for nome in ['maria', 'joana', 'luiz']:
     print(falar_bom_dia(nome))
     print(falar_boa_noite(nome))