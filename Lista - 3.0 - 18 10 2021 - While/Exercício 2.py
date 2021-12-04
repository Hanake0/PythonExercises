"""
Nome do desenvolvedor: Breno Gomes Haese - Hanake
Nome do programa: Faça um programa que leia um nome
    de usuário e a sua senha e não aceite a senha
    igual ao nome do usuário, mostrando uma mensagem
    de erro e voltando a pedir as informações.

Data: 18/10/2021
"""

# Entrada e processamento de dados
print("""
==========================================
          Validação de senha
==========================================
""")

usuario = ""
senha   = ""
while usuario == senha:
    usuario = input("Digite seu usuário: ")
    senha   = input("Digite sua senha: ")
    if usuario == senha:
        print("Usuário e senha não podem ser iguais!")
        print("")

# Saída de dados
print("""
==========================================
               Resultado
==========================================
""")

print("Usuario:    ", usuario)
print("Senha:      ", senha)
