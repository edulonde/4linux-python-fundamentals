nome = "Guido"
nr_pedido = 1457
minutos = 12
print("Olá  {nome}, seu pedido é o nº: {nr_pedido}, e chegará em até {minutos} minutos".format())


with open('filename', 'r') as arquivo:
conteudo = arquivo.read()