palavra_secreta = ['x', 'o', 't', 'a']
pl_user = []



tentativas = 0
while (set(pl_user) != set(palavra_secreta)):
    
    try:
        letra = input('digite uma letra: ')
        if letra in palavra_secreta:
            tentativas += 1
            pl_user += letra
            print(pl_user)
            continue
        else:
            print('*')
            tentativas += 1
            continue

    except ValueError:
        print('digite apenas letras.')
print(palavra_secreta)
print(tentativas)

    
