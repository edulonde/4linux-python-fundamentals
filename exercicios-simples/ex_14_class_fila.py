class Fila():
    def __init__(self):
        self.fila = []

    def adicionarPessoaNaFila(self):
        pessoa = int(input("Olá bem vindo a fila do Banco!"
              "qual a sua idade?"))
        if pessoa > 65:
            self.fila.insert(0,pessoa)
        else:
            self.fila.append(pessoa)

    def atenderFila(self):
        atendimento = self.fila[0]
        print (f'você está atendendo uma pessoa de {atendimento}')
        del self.fila[0]


f = Fila()
f.adicionarPessoaNaFila()
f.adicionarPessoaNaFila()
f.adicionarPessoaNaFila()
print(f.fila)
f.atenderFila()
print(f.fila)
f.atenderFila()
print(f.fila)