"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que leia 5
    números e informe o maior número.

Data: 18/10/2021
"""

# Entrada e processamento de dados
print("""
==========================================
          Maior entre 5 números
==========================================
""")

maiorNumero = float(input("Digite o 1º número: "))

num = 2
while num <= 5:
    numero = float(input("Digite o {}º número: ".format(num)))
    if numero > maiorNumero:
        maiorNumero = numero
    num += 1

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Maior:    ", maiorNumero)
