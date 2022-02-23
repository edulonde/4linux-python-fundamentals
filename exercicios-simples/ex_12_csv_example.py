# 2) Escreva um programa em python que realize um cadastro. Deverão ser coletadas as
# seguintes informações:
# • CPF / Nome /  Idade / Sexo / Endereço
# Os registros deverão ser armazenados em um arquivo CSV. Caso desejar manter o padrão
# brasileiro, o CSV será separado pelo caractere ;.

import csv

header = ['cpf','nome','idade','sexo','endereço']

with open('teste.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(header)

cpf = input("Digite seu cpf: ")
nome = input("Digite seu nome: ")
idade = input("Digite seu idade: ")
sexo = input("Digite seu sexo: ")
endereco = input("Digite seu endereço: ")

data =[]
data.append(cpf)
data.append(nome)
data.append(idade)
data.append(sexo)
data.append(endereco)

with open('teste.csv', 'a') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(data)