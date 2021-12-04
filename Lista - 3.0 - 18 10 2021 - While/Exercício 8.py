"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que leia 5
    números e informe a soma e a média dos números.

Data: 18/10/2021
"""

# Entrada e processamento de dados
print("""
==========================================
        Soma e media de 5 números
==========================================
""")

soma = 0
num = 1
while num <= 5:
    soma += float(input("Digite o {}º número: ".format(num)))
    num += 1

media = soma / 5
# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Soma:    ", soma)
print("Média:    {:.2f}".format(media))
