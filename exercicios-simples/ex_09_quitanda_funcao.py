cesta = []

def imprimir_menu():
    print("Quitanda:\n"
          "1 - ver cesta \n"
          "2 - adicionar frutas \n"
          "3 - carrinho \n"
          "4 - sair")

def imprimir_menu_frutas():
    print("Escolha a fruta desejada \n"
          "1 - banana \n"
          "2 - melancia \n"
          "3 - morango")

def processo_escolha(opcao):
    if opcao == 1:
        if len(cesta) == 0:
            print("Cesta vazia")
        else:
            print(cesta)
    elif opcao == 2:
        imprimir_menu_frutas()
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
    elif opcao == 4:
        print("Encerrando atendimento")
        exit()

while True:
    imprimir_menu()
    opcao = int(input("Digite a opção desejada:"))
    processo_escolha(opcao)

