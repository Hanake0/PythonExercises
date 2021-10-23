"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 8 - Faça um Programa
que peça 2 números inteiros e um número real.
Calcule e mostre:

 1. O produto do dobro do primeiro com metade do segundo .
 2. A soma do triplo do primeiro com o terceiro.
 3. O terceiro elevado ao cubo.


Data: 06/09/2021
"""

# Entrada de dados
print("""
==========================================
            Várias operações
==========================================
""")

nInteiro1 = int(input("Primeiro número inteiro: "))
nInteiro2 = int(input("Segundo número inteiro:  "))
nReal = float(input("Número Real:             "))

# Processamento de dados
resultado1 = (nInteiro1*2) * (nInteiro2/2)
resultado2 = (nInteiro1*3) + nReal
resultado3 = nReal**3

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
print("Resultado 3:", resultado3)
