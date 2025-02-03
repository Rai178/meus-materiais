compras = ['comp', 'mause', 'munitor', 'teclado', 'amd']
 
while True:
    user = input('Qual comando? [i]nserir, [a]pagar, [l]ista (digitar apenas letras.). Digite "sair" para sair.').lower()
    try:
        if user == 'i':
            inserir = input('inserir: ')
            compras.append(inserir)

        elif user == 'a':
            apagar = input('apagar(indice): ')
            del compras[int(apagar)]

        elif user == 'l':
            for indice, nome in enumerate(compras):
                print(indice, nome)

        elif user == 'sair':
            break

        else: 
            print('digite um valor válido.')
                
    except IndexError:
        print('fora do range. ')