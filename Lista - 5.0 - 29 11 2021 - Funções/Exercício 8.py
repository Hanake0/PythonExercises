"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça uma função que informe a quantidade de dígitos de
    um determinado número inteiro informado.

Data: 29/11/2021
"""


def qtd_digitos(num):
    """
    Função que informa a quantidade de dígitos de um determinado número inteiro
    :param num: Número inteiro
    :return: Quantidade de dígitos do número
    """

    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count
