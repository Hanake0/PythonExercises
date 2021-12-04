"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que peça as
    quatro notas de 10 alunos, calcule e armazene
    numa lista a média de cada aluno, imprima o
    número de alunos com média maior ou igual a 7.0.

Data: 16/11/2021
"""

# Entrada de dados
print("""
==========================================
          Calculo de Médias
==========================================
""")
notas = []
for i in range(10):
    n = []
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota do {i + 1}º aluno: "))
        n.append(nota)
    notas.append(n)

# Processamento de dados
acima = []
for n in notas:
    media = sum(n) / 4
    if media >= 7.0:
        acima.append(media)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Quantidade de Aluno Acima de 7.0:", len(acima))
print("Medias acima de 7.0:", acima)
