def contador():
    contagem = 0 # estado interno

    def incrementar():
        nonlocal contagem # acessa a var do escopo externo
        contagem += 1
        return contagem
    
    return incrementar

# criando o closure
contador_de_chamadas = contador()

# chamando a função e verificando a contagem 
print(contador_de_chamadas()) #saida: 1 
print(contador_de_chamadas()) #saida: 2
print(contador_de_chamadas()) #saida: 3