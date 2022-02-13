from calculadora import somar, dividir, multiplicar, diminuir

def main():


    op_validas = '1234'
operacoes = {
    '1': somar,
    '2': diminuir,
    '3': multiplicar,
    '4': diminuir
}
while True:
    print('Calculadora')
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
opcao = input("Escolha a operação desejada:\n1- Soma\n2- Subtração\n3-
Multiplicação\n4 - Divisão\n
")
if opcao in op_validas:
    print(operacoes[opcao](n1, n2))
else:
    print("Opção Inválida")
if input('Deseja Continuar? (S/N) ').upper() == 'N':
    break
if __name__ == '__main__':
    main()
