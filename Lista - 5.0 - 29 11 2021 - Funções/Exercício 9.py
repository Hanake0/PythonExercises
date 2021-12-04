"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Reverso do número.
    Faça uma função que retorne o reverso de um número inteiro informado.
    Por exemplo: 127 -> 721.

Data: 29/11/2021
"""


def reverso(num):
    """
    Função que retorna o reverso de um número inteiro informado.
    :param num: Número inteiro.
    :return: Reverso do número informado.
    """

    return int(str(num)[::-1])
