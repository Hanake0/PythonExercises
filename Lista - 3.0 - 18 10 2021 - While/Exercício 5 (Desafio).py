"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: (Desafio = 1 ponto) Altere o programa anterior
    permitindo ao usuário informar as populações e as taxas
    de crescimento iniciais. Valide a entrada e permita
    repetir a operação.

Data: 14/09/2021
"""

# Entrada de dados
print("""
==========================================
     Calculo de taxa de crescimento 2
==========================================
""")

popAsn = "n"
popA   = 0
while popAsn.lower() != "s":
    popA = float(input("Digite a população A:           "))
    popAsn = input(    "O valor está correto? [S/N]     ")
print("")

crescAsn = "n"
crescA   = 0
while crescAsn.lower() != "s":
    crescA = float(input("Digite a taxa de crescimento A: "))
    crescAsn = input(    "O valor está correto? [S/N]     ")
print("")


popBsn = "n"
popB   = 0
while popBsn.lower() != "s":
    popB = float(input("Digite a população B:           "))
    popBsn = input(    "O valor está correto? [S/N]     ")
print("")

crescBsn = "n"
crescB   = 0
while crescBsn.lower() != "s":
    crescB = float(input("Digite a taxa de crescimento B:"))
    crescBsn = input(    "O valor está correto? [S/N]    ")
print("")

# Processamento de dados
anos = 0
while popA < popB:
    popA += popA * crescA
    popB += popB * crescB
    anos += 1

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Tempo:", anos, "anos")
