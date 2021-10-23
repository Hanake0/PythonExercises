"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Programa 6 - Faça um Programa
que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
Segue a fórmula: C = (5 * (F-32) / 9).

Data: 06/09/2021
"""

# Entrada de dados
print("""
==========================================
      Conversão Para Graus Célsius
==========================================
""")

fahrenheit = float(input("Temperatura em Fahrenheit: "))

# Processamento de dados
celsius = (5*(fahrenheit-32))/9

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Fahrenheit:", fahrenheit, "°F")
print("Celsius:   ", celsius, "°C")
