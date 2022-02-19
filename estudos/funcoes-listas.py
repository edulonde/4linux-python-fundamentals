lista_numerica = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q,', 'r', 's', 't',
                'u', 'v', 'x', 'z']
lista_frutas = ['banana', 'maçã', 'pêra', 'melão', 'ameixa', 'romã']

# sort() e sorted()
lista_letras.sort(reverse=True)
print(lista_letras)
ordenando_lista = sorted(
    [125, 324, 256, 984, 12, 35, 65, 45, 78, 98, 65, 32, 45, 78, 15, 95, 123, 456, 89, 654, 789, 145])
print(ordenando_lista)

# split() - recorta uma string de acordo com um parâmetro passado
texto = "Jose Eduardo Santos Londe"
nome_recortado = texto.split(" ")
print(nome_recortado)

# append() - adiciona itens no final da lista
lista_frutas.append('Goiaba')

#insert() - adiciona item em posição desejada
lista_frutas.insert(2, "abacaxi")
lista_frutas.insert(5, "limão")


# len() - retorna o tamanho da lista como int
print(len(lista_frutas))
print(type(len(lista_frutas)))

#extend() - permite inserir uma lisat no final da outra lista
lista_frutas.extend(['morango','amora'])
print(lista_frutas,"e", len(lista_frutas), 'itens cadastrados.')

#index - permite descobrir a posição no index passando o identificador
print(lista_letras.index('j'))

#max(), min(), sum() e count()
print("Maior item: ",max(ordenando_lista))
print("Menor item: ",min(ordenando_lista))
print("Soma dos itens: ",sum(ordenando_lista))
print("Quantas vezes aparece o 'a' no alfabeto? ",lista_letras.count('a'))

#clear() - torna a lista vazia
lista_letras.clear()
print("lista vazia após o clear() :",lista_letras)

#pop() - exclui item em determinada posição
lista_frutas.pop(0)
print(lista_frutas)

#remove() - remove o primeiro item com o valor buscao
lista_numerica.remove("5")
print(lista_numerica)

#copy()
copia_lista_frutas = lista_frutas.copy()
print(copia_lista_frutas)