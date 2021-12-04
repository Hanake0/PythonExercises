"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que converta da notação de 24 horas
    para a notação de 12 horas.
    Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
    A entrada é dada em dois inteiros.
    Deve haver pelo menos duas funções:
    uma para fazer a conversão e uma para a saída.
    Registre a informação A.M./P.M. como um valor ‘A’
    para A.M. e ‘P’ para P.M.
    Assim, a função para efetuar as conversões terá um
    parâmetro formal para registrar se é A.M. ou P.M.
    Inclua um loop que permita que o usuário repita esse
    cálculo para novos valores de entrada todas as vezes
    que desejar.

Data: 29/11/2021
"""


# Funções
def convert(h):
    """
    Função que converte as horas de 24 para 12
    :param h: horas
    :return: h -> horas, a_p -> "A" ou "P"
    """

    n = int(h/12)
    h = h % 12

    if n % 2 == 0:
        a_p = "A"
    else:
        a_p = "P"

    return h, a_p


def print_result(h, m, a_p):
    """
    Função que imprime o resultado da conversão
    :param h: horas
    :param m: minutos
    :param a_p: "A" ou "P"
    :return: Não retorna nada
    """

    if a_p == "A":
        print(f"Resultado: {h}:{m} A.M.")
    elif a_p == "P":
        print(f"Resultado: {h}:{m} P.M.")
    else:
        print("Erro")


# Programa
print("""
==========================================
            Conversão de Horas
==========================================
""")

sair = False
while not sair:
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite os minutos: "))
    am_pm = ""
    print()

    hora, am_pm = convert(hora)
    print_result(hora, minuto, am_pm)
    print()

    sair = input("Deseja sair? [S/N] ").upper() == "S"
    print()
