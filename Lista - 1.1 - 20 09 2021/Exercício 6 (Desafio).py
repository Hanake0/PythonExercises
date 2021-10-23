"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa para uma loja
de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere
que a cobertura da tinta é de 1 litro para cada 6
metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de
3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem
compradas e os respectivos preços em 3 situações:
	* Comprar apenas latas de 18 litros;
	* Comprar apenas galões de 3,6 litros;
	* Misturar latas e galões, de forma que o preço
	  seja o menor. Acrescente 10% de folga nas
	  misturas (se necessário) e sempre arredonde os
	  valores para cima, isto é, considere latas cheias.


Data: 14/09/2021
"""
import math

# Entrada de dados
print("""
==========================================
        Cálculo de Uso de Tinta 2
==========================================
""")

area = float(input("Quantos m² a serem pintados: "))

# Processamento de dados
litros = area / 6

# Caso 1
c1Latas = math.ceil(litros / 18)
c1Litros = c1Latas * 18
c1Preco = float(c1Latas * 80)

# Caso 2
c2Galoes = math.ceil(litros / 3.6)
c2Litros = c2Galoes * 3.6
c2Preco = float(c2Galoes * 25)

# Caso 3
c3Latas = math.floor(litros / 18)
c3Galoes = 0

if (litros % 18) < 10.8:
	c3Galoes = math.ceil((litros - (c3Latas*18)) / 3.6)

else:
	c3Latas += 1

c3Litros = (c3Galoes * 3.6) + (c3Latas * 18)
c3Preco = float((c3Latas * 80) + (c3Galoes * 25))

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Area a ser pintada         :    ", area, "m²")
print("Litros de tinta necessários:    ", litros, "l")
print("")

print("Caso 1: Apenas Latas de tinta")
print("     Latas necessárias     :    ", c1Latas)
print("")
print("     Litros totais         :    ", c1Litros, "l")
print("     Preço Total           :  R$", c1Preco)
print("")

print("Caso 2: Apenas Galões de tinta")
print("     Galões necessários    :    ", c2Galoes)
print("")
print("     Litros totais         :    ", c2Litros, "l")
print("     Preço Total           :  R$", c2Preco)
print("")

print("Caso 3: Latas e Galões")
print("     Latas necessárias     :    ", c3Latas)
print("     Galões necessários    :    ", c3Galoes)
print("")
print("     Litros totais         :    ", c3Litros, "l")
print("     Preço Total           :  R$", c3Preco)
