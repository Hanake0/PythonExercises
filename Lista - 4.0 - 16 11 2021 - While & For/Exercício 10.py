"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia duas
    listas com 10 elementos cada. Gere um terceiro
    vetor de 20 elementos, cujos valores deverão
    ser compostos pelos elementos intercalados
    de duas  outras listas.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
          Intercalando Listas
==========================================
""")
lista1 = []
for i in range(10):
    lista1.append(int(input(f"Digite o {i+1}º valor da lista 1: ")))

lista2 = []
for i in range(10):
    lista2.append(int(input(f"Digite o {i+1}º valor da lista 2: ")))

# Processamento de dados
intercalado = []
for i in range(10):
    intercalado.append(lista1[i])
    intercalado.append(lista2[i])

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")
print("Lista1:", lista1)
print("Lista2:", lista2)
print("Intercalado:", intercalado)
