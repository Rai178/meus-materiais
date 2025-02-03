"""
valores padrão para parametros
ao definir uma função, os parametros podem
ter valores padrão. caso o valor não seja 
enviado para o parametro, o valor padrão será
usado.
refatorar: editar o seu codigo.
int declarado como 0 é 'visto' pelo programa como falsy.
todo parametro que vier apos de um valor padrao eu devo colocar um valor 
padrão tambem.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} + {y=} ', x + y )


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)