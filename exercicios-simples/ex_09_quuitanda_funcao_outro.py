
#dicionario de produtos
produtos_quitanda = {
    'Banana' : 3.50,
    'Melancia' : 7.50,
    'Morango' : 5.00
}

cestacliente = {
    '1' : 0,
    '2' : 0,
    '3' : 0
}

def cesta():
    print('\nCesta de compras: ')
    print('Banana : ' , cestacliente['1'] , ' Melancia : ' , cestacliente['2'] , ' Morango : ' , cestacliente['3'])

def adicionar_fruta(item):
    cestacliente[item] += 1
    print('\nFruta adicionada com sucesso!')

def checkout():
    total = cestacliente['1']*produtos_quitanda['Banana'] + cestacliente['2']*produtos_quitanda['Melancia'] + cestacliente['3']*produtos_quitanda['Morango']
    print('\nCheckout - Total de compras: R$', total)

#menu adicionar frutas    
def menu2():
    print('\nMenu de frutas:')
    print('Escolha fruta desejada:')
    print('1 - Banana')
    print('2 - Melancia')
    print('3 - Morango')
    op2 = input('Digite à opção desejada: ')
    if op2 in cestacliente.keys():
        adicionar_fruta(op2)
    else:
        print('\nOpção inválida')

opcoes = {
    '1' : cesta,
    '2' : menu2,
    '3' : checkout,
    '4' : exit
}

#Menu principal
def menu():
    while True:

        print('\nMenu')
        print('1: Ver cesta')
        print('2: Adicionar Frutas')
        print('3: Checkout')
        print('4: Sair')
        op = input('Escolha sua opção :')

        if op in opcoes.keys():
            opcoes[op]()
        else:
            print('\nOpção inválida')

menu()