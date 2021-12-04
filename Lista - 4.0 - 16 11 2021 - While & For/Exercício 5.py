"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia 20
    números inteiros e armazene-os numa lista.
    Armazene os números pares no vetor PAR e os
    números impares no vetor IMPAR.
    Imprima as três listas.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
          Separação de números
==========================================
""")
lista = []
PAR = []
IMPAR = []
for i in range(20):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

# Processamento de dados
for i in lista:
    if i % 2 == 0:
        PAR.append(i)
    else:
        IMPAR.append(i)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Lista:", lista)
print("Pares:", PAR)
print("Impares:", IMPAR)
