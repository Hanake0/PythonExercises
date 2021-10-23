"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Tendo como dados de entrada a
altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58

Data: 14/09/2021
"""

# Entrada de dados
print("""
==========================================
          Cálculo de Peso Ideal
==========================================
""")

altura = float(input("Sua altura(metros): "))

# Processamento de dados
pesoIdeal = (72.7 * altura) - 58

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Altura:    ", altura)
print("Peso Ideal:", pesoIdeal)
