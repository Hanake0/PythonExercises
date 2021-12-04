"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia uma
    lista A com 10 números inteiros, calcule e
    mostre a soma dos quadrados dos elementos
    da lista.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
      Cálculo da Soma dos Quadrados
==========================================
""")
A = []
for i in range(10):
    A.append(int(input(f"Informe o {i + 1}º número: ")))

# Processamento de dados
quadrados = []
for i in A:
    quadrados.append(i ** 2)
soma = sum(quadrados)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")
print("Lista:", A)
print("Quadrados:", quadrados)
print("Soma dos quadrados:", soma)
