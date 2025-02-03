"""
escopo de funcoes em python
escopo significa o local onde aquele codigo pode atingir.
existe o escopo global e local.
o escopo global é o escopo onde todo o codigo é alcançavel.
o escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcancados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variavel do escopo externo
ser a mesma no escopo interno.
"""

x = 1

def escopo():
    # global x
    x = 10


    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)