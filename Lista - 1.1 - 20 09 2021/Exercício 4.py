"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um Programa que pergunte
quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para
o INSS e 5% para o sindicato, faça um programa
que nos dê:

 a. salário bruto.
 b. quanto pagou ao INSS.
 c. quanto pagou ao sindicato.
 d. o salário líquido.
 e. calcule os descontos e o salário líquido,
    conforme a tabela abaixo:
		+ Salário Bruto : R$
		- IR (11%) : R$
		- INSS (8%) : R$
		- Sindicato (5%) : R$
		= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

Data: 14/09/2021
"""

# Entrada de dados
print("""
==========================================
       Cálculo de Salário Liquido
==========================================
""")

salarioHora = int(input("Quantas horas você trabalhou no mês: "))
horas = float(input("Quanto você recebe por hora:        "))

# Processamento de dados
salarioBruto = salarioHora * horas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (impostoRenda + inss + sindicato)

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print(" + Salário Bruto  :   R$", salarioBruto)
print("")
print(" - IR (11%)       :   R$", impostoRenda)
print(" - INSS (8%)      :   R$", inss)
print(" - Sindicato (5%) :   R$", sindicato)
print("")
print(" = Salário Liquido:   R$", salarioLiquido)



