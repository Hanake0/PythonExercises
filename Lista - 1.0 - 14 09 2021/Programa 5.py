"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 5 - Faça um Programa
que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.

Data: 06/09/2021
"""

# Entrada de dados
print("""
==========================================
            Cálculo de Salário
==========================================
""")

base = float(input("Quanto você recebe por hora: R$ "))
tempo = int(input("Quantas horas você trabalha por mês: "))

# Processamento de dados
salario = base*tempo

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Salário: ", salario)
