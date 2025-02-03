# def fatorial(num=1):
#     resultado = 1
#     for i in range(1, num + 1):
#         resultado *= i
#     return resultado

# print(fatorial(5))

def produtos_pares(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i * 2

    return resultado


print(produtos_pares(3))




