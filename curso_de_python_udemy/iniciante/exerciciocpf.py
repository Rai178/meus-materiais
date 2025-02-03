"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite seu cpf sem traços e pontos.')
digitos_cpf = []
for numero in cpf:
    digitos_cpf.append(int(numero))

m2 = digitos_cpf[0] * 10 
m3 = digitos_cpf[1] * 9 
m4 = digitos_cpf[2] * 8 
m5 = digitos_cpf[3] * 7 
m6 = digitos_cpf[4] * 6 
m7 = digitos_cpf[5] * 5 
m8 = digitos_cpf[6] * 4 
m9 = digitos_cpf[7] * 3 
m10 = digitos_cpf[8] * 2 
r0 = m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10
r1 = r0  * 10
r2 = r1 % 11

if r2 > 9:
    resultado = 0
else:
    print(r2)

