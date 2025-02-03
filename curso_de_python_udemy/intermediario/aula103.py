# funcoes decoradoras e decoradores
# decorar = adicionar / remover / restringir / alterar
# funcoes decoradoras são funcoes que decoram outras funcoes
# decoradores são usados para fazer o python
# usar as funcoes decoradoras em outras funcoes.
# decoradores são "syntax sugar" (acucar sintatico)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        resultado += 'qualquer'
        print(f'o seu resultado foi {resultado}')
        print('ok, agora voce foi decorada')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)