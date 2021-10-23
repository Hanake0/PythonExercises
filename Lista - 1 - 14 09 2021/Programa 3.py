"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 3 - Faça um Programa que
peça o raio de um círculo, calcule e mostre sua área.

Data: 06/09/2021
"""

# Constantes
pi = 3.1415

# Entrada de dados
print("""
==========================================
      Cálculo da Area de um Círculo
==========================================
""")

raio = float(input("Raio do círculo: "))

# Processamento de dados
area = pi*(raio**2)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Area: ", area)
