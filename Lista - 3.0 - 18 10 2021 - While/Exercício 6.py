"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que imprima
    na tela os números de 1 a 20, um abaixo do
    outro. Depois modifique o programa para que
    ele mostre os números um ao lado do outro.

Data: 18/10/2021
"""

# Saída e processamento de dados
print("""
==========================================
          Números de 1 a 20
==========================================
""")

num = 1
while num <= 20:
    print(num)
    num += 1

print("")

numeros = ""
num = 1
while num <= 20:
    numeros += str(num) + " "
    num += 1

print(numeros)
