"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Jogo de Craps.
    Faça um programa de implemente um jogo de Craps.
    O jogador lança um par de dados, obtendo um valor entre 2 e 12.
    Se, na primeira jogada, você tirar 7 ou 11, você tirou um "natural" e ganhou.
    Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
    Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".
    Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
    Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

Data: 29/11/2021
"""

import random


# Funçoes
def jogar_dados():
    """
    Função que simula o lançamento de dados.
    :return: Retorna um valor entre 2 e 12.
    """

    return random.randint(1, 6) + random.randint(1, 6)


def primeira_jogada():
    """
    Função que simula a primeira jogada.
    :return: Retorna 1 se o jogador tiver vencido, -1 se tiver perdido, ou o seu "Ponto" caso contrário.
    """

    dados = jogar_dados()
    print(f'Você tirou {dados}')

    if dados in (7, 11):
        return 1
    elif dados in (2, 3, 12):
        return -1
    else:
        return dados


# Programa
print("""
==========================================
              Jogo de Craps
==========================================
""")

ponto = primeira_jogada()

if ponto == -1:
    print("Craps! Você perdeu!")

elif ponto == 1:
    print("Tirou um natural! Você ganhou!")

else:
    print(f"Seu Ponto agora é {ponto}!")
    print("Vamos continuar jogando ate tirar esse numero novamente...")
    print()

    atual = 0
    while atual != ponto:
        atual = jogar_dados()
        print(f"Você tirou {atual}")

        if atual == 7:
            print("Você perdeu!")
            break
    else:
        print("Você ganhou!")