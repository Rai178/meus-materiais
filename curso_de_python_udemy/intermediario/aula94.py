# try, except, else e finally
try:
    print('abrir arquivo')
    # 8/0
except ZeroDivisionError:
    print('dividiu zero')
else:
    print('nao deu erro')
finally:
    print('fechar arquivo')