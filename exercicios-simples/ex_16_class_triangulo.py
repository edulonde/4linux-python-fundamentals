class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def perimetro(self):
        perimetro = self.lado_a + self.lado_b + self.lado_c
        print("O perímetro é: ", perimetro)

    def maiorlado(self):
        lista_lados = [self.lado_a, self.lado_b, self.lado_c]
        print("O maior lado é: ", max(lista_lados))


triangulo_1 = Triangulo(3, 4, 5)
triangulo_1.perimetro()
triangulo_1.maiorlado()
