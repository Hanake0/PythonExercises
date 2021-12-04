"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia uma
    lista de 5 números inteiros, mostre a soma,
    a multiplicação e os números.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
          Operaçoes com listas
==========================================
""")
lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i+1}º numero: ")))

# Processamento de dados
soma = sum(lista)
multiplicacao = 1
for i in lista:
    multiplicacao *= i

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Lista:", lista)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
