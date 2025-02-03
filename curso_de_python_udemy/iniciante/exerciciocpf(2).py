"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77  40 54 64 14 24 40 36 0 14

Somar todos os resultados: 
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 0
"""

cpf = '7468248907'
digitos_cpf = []
for numero in cpf:
    digitos_cpf.append(int(numero))
m1 = digitos_cpf[0] * 11
m2 = digitos_cpf[1] * 10 
m3 = digitos_cpf[2] * 9 
m4 = digitos_cpf[3] * 8 
m5 = digitos_cpf[4] * 7 
m6 = digitos_cpf[5] * 6 
m7 = digitos_cpf[6] * 5 
m8 = digitos_cpf[7] * 4 
m9 = digitos_cpf[8] * 3 
m10 = digitos_cpf[9] * 2 
r0 =  m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10
r1 = r0  * 10
r2 = r1 % 11

if r2 > 9:
    resultado = 0
else:
    print(r2)