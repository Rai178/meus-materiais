import os

lista = []
while True:
    print('selecione uma opçao')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('valor: ')
        lista.append(valor)
    
    elif opcao == 'a':
        indice_str = input(
            'escolha o indice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('nao foi possivel apagar este indice')
        except IndexError:
            print('nao foi possivel apagar este indice')
        except Exception:
            print('nao sei oq aconteceu ')

    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('por favor escolha um valor valido.')

   
    