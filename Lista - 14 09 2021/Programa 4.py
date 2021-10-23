"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 4 - Faça um Programa que
calcule a área de um quadrado, em seguida mostre o
dobro desta área para o usuário.

Data: 06/09/2021
"""

# Entrada de dados
print("""
==========================================
      Cálculo da Area de um Quadrado
==========================================
""")

lado = float(input("Lado do quadrado: "))

# Processamento de dados
area = lado*lado
dobro = area*2

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Área:          ", area)
print("Dobro da área: ", dobro)
