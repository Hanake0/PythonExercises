"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que peça a idade
    e a altura de 5 pessoas, armazene cada
    informação em sua respectiva lista.
    Imprima a idade e a altura na ordem inversa a
    ordem lida.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
            Inversao de Dados
==========================================
""")
idades = []
alturas = []
for i in range(5):
    idades.append(int(input(f"Informe a idade da {i + 1}ª pessoa: ")))
    alturas.append(float(input(f"Informe a altura da {i + 1}ª pessoa: ")))
    print("")

# Processamento de dados
idades.reverse()
alturas.reverse()

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")
for i in range(5):
    print(f"Idade: {idades[i]}")
    print(f"Altura: {alturas[i]}")
    print("")
