texto = " Esse texto será lido letra a letra por uma iteração através de um for e " \
        "será feito a contagem das vogais. Depois esse texto será armazenado em um arquivo txt"
vogais = ['a','e','i','o','u']



def contar_vogais():
    contador = 0
    for c in texto:
        if c.lower() in vogais:
            contador = contador + 1
    print(contador)
contar_vogais()


with open('arquivo-teste.txt', 'w') as arquivo:
    arquivo.write(texto)