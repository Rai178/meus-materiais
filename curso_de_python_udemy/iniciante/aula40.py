""" calculadora com while """
while True:
    nu1 = input('digite um número: ')
    nu2 = input('digite outro: ')

    n1 = int(nu1)
    n2 = int(nu2)
    
    soma = n1 + n2
    multiplicacao = n1 * n2
    subtracao = n1 - n2
    divisao = n1 / n2
    potencia = n1 ** n2
    while True:
        operacao = input("Qual operação: * / ** + - %: ")
        if operacao == '+':
            print(soma)
            break
        elif operacao == '-':
            print(subtracao)
            break
        elif operacao == '/':
            print(divisao)
            break
        elif operacao == '*':
            print(multiplicacao)
            break
        elif operacao == '**':
            print(potencia)
            break
        else:
            print('digite uma operação valida')

    sair = input('quer sair? [s]im: ').lower().startswith('s')
    
    if sair == True:
        break

    
    