
def calc(y):
    def calc2(x):
        x = x * y
        return x
    return calc2

quadriplicar = calc(4)
triplicar = calc(3)
duplicar = calc(2)

print(quadriplicar(2))