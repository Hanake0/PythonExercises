"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que use a função valorPagamento para
    determinar o valor a ser pago por uma prestação de uma conta.
    O programa deverá solicitar ao usuário o valor da prestação
    e o número de dias em atraso e passar estes valores
    para a função valorPagamento, que calculará o valor a
    ser pago e devolverá este valor ao programa que a chamou.
    O programa deverá então exibir o valor a ser pago na tela.
    Após a execução o programa deverá voltar a pedir outro
    valor de prestação e assim continuar até que seja informado
    um valor igual a zero para a prestação.
    Neste momento o programa deverá ser encerrado,
    exibindo o relatório do dia, que conterá a quantidade
    e o valor total de prestações pagas no dia.
    O cálculo do valor a ser pago é feito da seguinte forma:
     - Para pagamentos sem atraso, cobrar o valor da prestação.
     - Quando houver atraso, cobrar 3% de multa,
       mais 0,1% de juros por dia de atraso.

Data: 29/11/2021
"""


# Funções
def valorPagamento(valor, dias):
    """
    Função que calcula o valor a ser pago de acordo com o valor da prestação e os dias em atraso.
    :param valor: Valor da prestação.
    :param dias: Dias em atraso.
    :return: Retorna o valor a ser pago.
    """

    if dias > 0:
        valor += (valor * 0.001 * dias)
        valor += (valor * 0.030)
    return valor


def relatorio(prestacoes, t):
    """
    Função que exibe o relatório do dia.
    :param prestacoes: Quantidade de prestações pagas.
    :param t: Valor total pago.
    :return: Não retorna nada.
    """

    print()
    print()
    print(f'Valor pago hoje: R${t:.2f}')
    print(f'Nr de prestações pagas hoje: {prestacoes}')


# Programa
print("""
==========================================
         Pagamento de prestações
==========================================
""")

prestações = 0
total = 0

valor = float(input('Digite o valor da prestação: R$ '))
while valor != 0:
    dias = int(input('Digite o número de dias em atraso: '))
    valor = valorPagamento(valor, dias)

    prestações += 1
    total += valor

    print()
    print(f'Valor a ser pago: R${valor:.2f}')
    print()

    valor = float(input('Digite o valor da prestação: R$'))

relatorio(prestações, total)
