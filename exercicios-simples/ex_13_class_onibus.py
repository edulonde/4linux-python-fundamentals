class Onibus():
    def __init__(self):
        self.lotacao_max = 45
        self.lotacao_atual = 0
        self.velocidade = 0
        self.placa = " "
        self.modelo = " "

    def acelerar(self, velocidade):
        velocidade = velocidade + 10
        print(velocidade)

    def frear(self, velocidade):
        velocidade = velocidade - 10
        print(velocidade)

    def embarcar(self, lotacao_max, lotacao_atual):
        if lotacao_max == 45:
            print("o busão está cheio")
        else:
            lotacao_atual = lotacao_atual + 1

    def desembarcar(self, lotacao_atual):
        if lotacao_atual == 0:
            print("Não tem mais passageiro para desembarcar")
        else:
            lotacao_atual = lotacao_atual - 1


onibus_123 = Onibus()
onibus_123.acelerar(velocidade=60)
onibus_123.frear(velocidade=60)
onibus_123.lotacao_atual = 20
onibus_123.embarcar(lotacao_max=45,lotacao_atual=20)