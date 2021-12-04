"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que peça uma
    nota, entre zero e dez. Mostre uma mensagem
    caso o valor seja inválido e continue pedindo
    até que o usuário informe um valor válido.

Data: 18/10/2021
"""

# Entrada e processamento de dados
print("""
==========================================
            Validação de nota
==========================================
""")

nota = -1
while nota < 0 or nota > 10:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Nota inválida!")
        print("")
    else:
        print("Nota válida!")

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Nota:    ", nota)
