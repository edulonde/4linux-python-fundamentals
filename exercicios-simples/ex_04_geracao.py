# 1) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração a qual a pessoa pertence.

ano_de_nascimento = int(input("Digite seu ano de nascimento:"))

if ano_de_nascimento <= 1964:
    print("Baby Boomer")
elif ano_de_nascimento <= 1979:
    print("Geração X")
elif ano_de_nascimento <= 1994:
    print("Geração Y")
else:
    print ("Geração Z")




