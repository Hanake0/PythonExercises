"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que leia uma
    lista de 10 números reais e mostre-os na
    ordem inversa.

Data: 16/11/2021
"""

# Entrada e processamento de dados
print("""
==========================================
            Leitura de Lista
==========================================
""")
lista = []
for i in range(10):
    lista.append(float(input(f"Digite o {i+1}º número: ")))

lista.reverse()

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Lista:", lista)
