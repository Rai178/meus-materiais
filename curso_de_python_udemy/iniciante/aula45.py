"""
iterável => str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador 
"""
#for letra in texto
texto = 'luiz' # iteravel
# iterador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
        # break

for letra in texto:
    print(letra)