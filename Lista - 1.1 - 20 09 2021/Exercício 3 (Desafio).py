"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: João Papo-de-Pescador, homem de
bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que
ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado
de São Paulo (50 quilos) deve pagar uma multa de
R$ 4,00 por quilo excedente. João precisa que você
faça um programa que leia a variável peso (peso de
peixes) e verifique se há excesso. Se houver,
gravar na variável excesso e na variável multa o
valor da multa que João deverá pagar. Caso contrário
mostrar tais variáveis com o conteúdo ZERO.
(DESAFIO :)

Data: 14/09/2021
"""
import math

# Entrada de dados
print("""
==========================================
       Cálculo de Excedente de Peso
==========================================
""")

peso = float(input("Quantos quilos foi pescado: "))

# Processamento de dados
excesso = 0

if peso > 50:
	excesso = peso - 50

multa = float(math.floor(excesso) * 4)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

if math.floor(peso) > 50:
	print("Houve excesso de peso!")

else:
	print("Não houve excesso de peso.")

print("Peso pescado:", peso, "kg")
print("Excesso:     ", excesso, "kg")
print("Multa:     R$", multa)
