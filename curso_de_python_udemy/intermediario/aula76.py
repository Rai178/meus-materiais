"""
dicionarios em python (tipo dict)
dicionarios são estruturas de dados do tipo 
par de "chave" e "valor".
chaves podem ser consideradas como o "indice"
que vimos na lista e podem ser de tipos imutáveis 
como: str, int, float, bool, tuple, etc.
o valor pode ser de qualquer tipo, incluindo outro dicionario.
usamos as chaves - {} - ou a classe dict para criar dicionarios.
imutáveis: str, int, float, bool, tuple
mutável: dict, list
pessoa = {
    'nome': 'luiz otavio',
    'sobrenome': 'miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}
"""
# pessoa = dict(nome='luiz otavio', sobrenome='miranda')

pessoa = {
    'nome': 'luiz otavio',
    'sobrenome': 'miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}

print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])