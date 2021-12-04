"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que leia e
    valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';

Data: 18/10/2021
"""

# Entrada e processamento de dados
print("""
==========================================
           Validação de dados
==========================================
""")

nome = ""
while len(nome) < 3:
    nome = input("Nome[>3]: ")
    if len(nome) < 3:
        print("Nome inválido!")
print("")

idade = 0
while idade <= 0 or idade >= 150:
    idade = int(input("Idade[>0 & <150]: "))
    if idade < 0 or idade > 150:
        print("Idade inválida!")
print("")

salario = 0
while salario <= 0:
    salario = float(input("Salário[>0]: "))
    if salario <= 0:
        print("Salário inválido!")
print("")

sexo = ""
while sexo != "f" and sexo != "m":
    sexo = input("Sexo[f/m]: ")
    if sexo != "f" and sexo != "m":
        print("Sexo inválido!")
print("")

estado_civil = ""
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Estado Civil[s/c/v/d]: ")
    if estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
        print("Estado Civil inválido!")
print("")

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Nome:         ", nome)
print("Idade:        ", idade)
print("Salário:      ", salario)
print("Sexo:         ", sexo)
print("Estado Civil: ", estado_civil)
