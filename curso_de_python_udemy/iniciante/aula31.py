"""
Flag (Bandeira) - Marcar um local
Nome = não valor 
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condição = True
passou_no_if = None

if condição:
    passou_no_if = True
    print('Faça algo')
else:
    
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('não passou no if')

if passou_no_if is not None:
    print('passou no if')