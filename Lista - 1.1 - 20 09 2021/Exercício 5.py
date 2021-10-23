"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa para uma loja
de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere
que a cobertura da tinta é de 1 litro para cada 3
metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao
usuário a quantidades de latas de tinta a serem
compradas e o preço total.

Data: 14/09/2021
"""
import math

# Entrada de dados
print("""
==========================================
         Cálculo de Uso de Tinta
==========================================
""")

area = float(input("Quantos m² a serem pintados: "))

# Processamento de dados
litros = area / 3
latas = math.ceil(litros / 18)
preco = float(latas*80)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Area a ser pintada         :    ", area, "m²")
print("Litros de tinta necessários:    ", litros, "l")
print("Latas de tinta necessárias :    ", latas)
print("")
print("Preço Total                :  R$", preco)
