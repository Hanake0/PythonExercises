"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia uma
    lista de 10 caracteres, e diga quantas
    consoantes foram lidas.
    Imprima as consoantes.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
          Contagem de consoantes
==========================================
""")
lista = []
for i in range(10):
    lista.append(input(f"Digite o {i+1}º caractere: "))

# Processamento de dados
consoantes = []
for c in lista:
    if c.lower() in "bcdfghjklmnpqrstvwxyz":
        consoantes.append(c)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Consoantes:", consoantes)
print("Quantidade de Consoantes:", len(consoantes))
