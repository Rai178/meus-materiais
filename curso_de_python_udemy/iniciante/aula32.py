# numero_int = input("numero inteiro: ")

# try:
#     if int(numero_int) % 2 == 0:
#         print("esse número é par")
#     elif int(numero_int % 2) != 0:
#         print("esse número não é par")

# except ValueError:
#     print("esse número não é um inteiro, digite um inteiro.")

# hora = int(input("que horas são?"))

# if 0 <= hora <= 11:
#     print("Bom dia") 
# elif 12 <= hora <= 17:
#     print("boa tarde")
# elif 18 <= hora <= 23:
#     print("boa noite")

nome = input("digite seu nome ")

if len(nome) < 4:
    print("seu nome é curto")
elif 5 <= len(nome) <= 6:
    print("seu nome é normal")
elif 6 < len(nome):
    print("seu nome é grande")

