"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia uma
    lista de 5 números inteiros e mostre-os.

Data: 16/11/2021
"""

# Entrada e processamento de dados
print("""
==========================================
             Leitura de Lista
==========================================
""")
lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i+1}º número: ")))


# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Lista:", lista)