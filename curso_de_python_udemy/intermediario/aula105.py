# decoradores com parametros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('decoradora 1')

        def aninhada(*args, **kwargs):
            print('parametros do decorador, ', a, b, c)
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

   


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)