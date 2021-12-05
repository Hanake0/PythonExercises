"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 7 - Faça um Programa
que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
Neste caso, vocês vão procurar a fórmula!

Data: 06/09/2021
"""

# Entrada de dados
print("""
==========================================
      Conversão Para Graus Fahrenheit
==========================================
""")

celsius = float(input("Temperatura em Celsius: "))

# Processamento de dados
fahrenheit = (celsius*9/5) + 32

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Celsius:   ", celsius, "°C")
print("Fahrenheit:", fahrenheit, "°F")
