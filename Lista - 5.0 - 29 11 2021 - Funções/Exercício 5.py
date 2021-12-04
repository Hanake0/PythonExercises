"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa com uma função chamada somaImposto.
    A função possui dois parâmetros formais: taxaImposto,
    que é a quantia de imposto sobre vendas expressa em
    porcentagem e custo, que é o custo de um item antes
    do imposto. A função “altera” o valor de custo para
    incluir o imposto sobre vendas.

Data: 29/11/2021
"""


def somaImposto(taxaImposto, custo):
    """
    Função que calcula o custo de um item com imposto.
    :param taxaImposto: Taxa de imposto sobre vendas.
    :param custo: Custo do item antes do imposto.
    :return: Custo do item com imposto.
    """

    custo = custo + (custo * taxaImposto)
    return custo
