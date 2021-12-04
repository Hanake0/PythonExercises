"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa, com uma função
    que necessite de um argumento.
    A função retorna o valor de caractere ‘P’, se seu
    argumento for positivo, e ‘N’, se seu argumento for
    zero ou negativo.

Data: 29/11/2021
"""


def positivo_negativo(numero):
    """
    Função que retorna o valor de caractere 'P' se seu argumento for positivo,
    e 'N' se seu argumento for zero ou negativo.
    :param numero: um número inteiro
    :return: um caractere 'P' ou 'N'
    """

    if numero > 0:
        return 'P'
    else:
        return 'N'
