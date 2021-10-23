"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 1 - Faça um Programa que peça
as 4 notas bimestrais e mostre a média.

Data: 06/09/2021
"""

# Entrada de dados
print("""
==========================================
      Cálculo de Média entre 4 notas
==========================================
""")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

# Processamento de dados
soma = nota1 + nota2 + nota3 + nota4
media = soma/4

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("A média é: ", media)
