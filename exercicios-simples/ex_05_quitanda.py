# Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras e retornar preço total.

menu = ("Quitanda:\n"
        "1 - ver cesta \n"
        "2 - adicionar frutas \n"
        "3 - carrinho \n"
        "4 - sair")

menu_de_frutas = ("Escolha a fruta desejada \n"
                  "1 - banana \n"
                  "2 - melancia \n"
                  "3 - morango")
cesta = []
controle = 1
while controle:
    print(menu)
    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        if len(cesta) == 0:
            print("Cesta vazia")
        else:
            print(cesta)
    elif opcao == 2:
        print(menu_de_frutas)
        opcao_fruta = int(input("Digite a opção desejada:"))
        if opcao_fruta == 1:
            cesta.append({"banana": 3.50})
            print("banana adicionada!")
        elif opcao_fruta == 2:
            cesta.append({"melancia": 7.50})
            print("melancia adicionada!")
        elif opcao_fruta == 3:
            cesta.append({"morango": 5.00})
            print("morango adicionado!")
    elif opcao == 3:
        preco_total = []
        for item in cesta:
            for valor in item.values():
                preco_total.append(valor)
        print(sum(preco_total))
else:
    controle = 0
