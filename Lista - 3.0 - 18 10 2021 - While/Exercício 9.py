"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que imprima
na tela apenas os números ímpares entre 1 e 50.

Data: 18/10/2021
"""

print("""
==========================================
            Ímpares entre 1 e 50
==========================================
""")

# Processamento e saída de dados

num = 2;
while num < 50:
    if num % 2 != 0:
        print(num)
    num += 1