
nome = input("Digite seu nome: ")
cpf = input(str("Digite seu CPF: "))
idade = input("Digite sua idade: ")


def imprimir_confirmacao_cadastro ():
    print('-' * 25)
    print(f"Configuração de Cadastro: \n "
          f"NOME: {nome} \n"
          f"CPF: {cpf} \n"
          f"IDADE: {idade} \n")
    print('-' * 25)

imprimir_confirmacao_cadastro()