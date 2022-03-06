class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def gratificacao(self, aumento):
        porcentagem = aumento / 100
        self.salario = self.salario * porcentagem
        print(f"O bônus para o funcionário {self.nome} foi de {self.salario}")


funcionario_1 = Funcionario('Harry', 5000)
funcionario_1.gratificacao(10)
