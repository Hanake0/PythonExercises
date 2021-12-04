"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: (Desafio = 1 ponto) Supondo que
    a população de um país A seja da ordem de
    80000 habitantes com uma taxa anual de
    crescimento de 3% e que a população de B seja
    200000 habitantes com uma taxa de crescimento
    de 1.5%.

    Faça um programa que calcule e escreva o
    número de anos necessários para que a população
    do país A ultrapasse ou iguale a população do
    país B, mantidas as taxas de crescimento.

Data: 14/09/2021
"""

print("""
==========================================
      Calculo de taxa de crescimento
==========================================
""")

# Processamento de dados
popA   = 80000
popB   = 200000
crescA = 0.030
crescB = 0.015

anos = 0
while popA < popB:
    popA += popA * crescA
    popB += popB * crescB
    anos += 1

# Saída de dados
print("Tempo:", anos, "anos")
