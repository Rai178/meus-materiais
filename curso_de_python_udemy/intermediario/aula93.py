# try, except, else e finally

# c = a / b

try:
    a = 18
    b = 0
    print('linha 1')
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('msg:', error)
    print('nome:', error.__class__.__name__)
except Exception:
    print('erro desconhecido.')

print('continuar')