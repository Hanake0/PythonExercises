"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Tendo como dados de entrada a
altura e o sexo de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando
as seguintes fórmulas:
 a. Para homens: (72.7*h) - 58
 b. Para mulheres: (62.1*h) - 44.7 (h = altura)
 c. Peça o peso da pessoa e informe se ela está
    dentro, acima ou abaixo do peso.

Data: 14/09/2021
"""

# Entrada de dados
print("""
==========================================
          Cálculo de Peso Ideal
==========================================
""")

sexo = str(input("Seu sexo(m ou f): "))
altura = float(input("Sua altura(metros): "))
peso = float(input("Seu peso(kg): "))

# Processamento de dados
pesoIdeal = -1

if sexo.lower() == "f":
	pesoIdeal = (62.1 * altura) - 44.7

elif sexo.lower() == "m":
	pesoIdeal = (72.7 * altura) - 58

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

if pesoIdeal == -1:
	print("Opção de sexo inválida !")

else:
	if peso > pesoIdeal:
		print("Você está acima do peso ideal!")

	elif peso == pesoIdeal:
		print("Você está com o peso ideal.")

	elif peso < pesoIdeal:
		print("Você está abaixo do peso ideal!")

	print("Altura:    ", altura)
	print("Peso:      ", peso)
	print("Peso Ideal:", pesoIdeal)
