# exemplo de uso dos sets
letras = set()
while True:
    letra = input('digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabens')
        break

    print(letras)
