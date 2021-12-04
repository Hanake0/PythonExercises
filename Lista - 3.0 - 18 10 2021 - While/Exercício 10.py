"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que receba dois
    números inteiros e gere os números inteiros
    que estão no intervalo compreendido por eles.

Data: 18/10/2021
"""

# Entrada de dados
print("""
==========================================
           Intervalo de números
==========================================
""")

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

# Processamento e saída de dados
print("""
==========================================
               Resultado
==========================================
""")

num = inicio+1
while num < fim:
    print(num)
    num += 1