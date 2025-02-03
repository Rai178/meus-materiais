palavra_secreta = 'perfume'
letra_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letra_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('vc ganhou  ')
        print('a palavra era ', palavra_secreta)
        print('tentativas ', tentativas)
        letra_acertadas = ''
        numero_tentativas = 0
