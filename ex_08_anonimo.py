n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = lambda n1, n2: n1 + n2
sub = lambda n1, n2: n1 - n2
div = lambda n1, n2: (n1 / n2)
mult = lambda n1, n2: (n1 * n2)

print(f"A soma de {n1} e {n2} é: ", soma(n1, n2))
print(f"A subtração de {n1} e {n2} é: ", sub(n1, n2))
print(f"A divisão de {n1} e {n2} é: ", div(n1, n2))
print(f"A multiplicação de {n1} e {n2} é: ", mult(n1, n2))
