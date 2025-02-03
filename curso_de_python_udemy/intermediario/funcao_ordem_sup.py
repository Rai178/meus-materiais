
#funcao de ordem sup que recebe outra como arg.

def aplicar_operacao(funcao, valor):
    return funcao(valor)

def quadrado(x):
    return x * x

def cubo(x):
    return x * x * x

#passando funcoes como argumento
#funcao aplicar_operacao é uma funcao de ordem superior porque recebe uma
#funcao como argumento
print(aplicar_operacao(quadrado, 5))
print(aplicar_operacao(cubo, 2))

#funcao de ordem sup que retorna outra funcao

def saudacao_personalizada(saudacao):
    def saudar(nome):
        return(f"{saudacao}, {nome}!")
    return saudar

#criando funcoes personalizadas
saudar_ola = saudacao_personalizada("ola")
saudar_bom_dia = saudacao_personalizada("bom dia")

print(saudar_ola("carlos"))
print(saudar_bom_dia("ana"))

#map, filter e reduce

    #map: 
    # aplica uma funcao a cada item do iteravel e retorna um novo iteravel

def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
dobrados = map(dobrar, numeros)

print(list(dobrados)) # saida: [2, 4, 6, 8, 10]

    #filter:
    # aplica uma fun que retorna true ou false a cada item do iteravel e 
    #retorna os iter trues

def eh_par(x):
    return x % 2 == 0 

numeros = [1, 2, 3, 4, 5]
pares = filter(eh_par, numeros)

print(list(pares)) 


    #reduce:
    # fun de forma acumulativa em todos os items, reduzindo a um.

from functools import reduce

def soma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]
soma_total = reduce(soma, numeros)

print(soma_total)
