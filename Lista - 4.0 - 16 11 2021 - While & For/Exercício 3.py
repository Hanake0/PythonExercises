"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia 4
    notas, mostre as notas e a média na tela
    (utilizando lista).

Data: 16/11/2021
"""

# Entrada e processamento de dados
print("""
==========================================
            Leitura de Notas
==========================================
""")
lista = []
for i in range(4):
    lista.append(float(input(f"Digite a {i + 1}ª nota: ")))

media = sum(lista) / 4

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Lista:", lista)
print("Media:", media)
