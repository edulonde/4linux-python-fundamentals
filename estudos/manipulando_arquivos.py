#cria um arquivo
with open("novo_arquivo.txt", "w") as novo_arquivo:
    novo_arquivo.write("Nunca foi tão fácil criar um arquivo.")

#cria uma arquivo html
# with open("pagina.html", "w") as pagina:
#     pagina.write("<body> <h1> Esta é um teste para página WEB </h1>")
#     pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:  </h2>")
#     pagina.write("<h3>")
#     nome=""
#     while nome!="SAIR":
#         nome = input("Digite um nome ou SAIR: ").upper()
#         if nome!="SAIR":
#             pagina.write("<br>"+nome)
#     pagina.write("</h3></body>")


with open("pagina.html", "r") as arquivo:
    conteudo=arquivo.read()
print("Tipo de dado da variável",type(conteudo))
print("Conteúdo do arquivo: ",conteudo)

#busca index da primeira ocorrencia de uma determinada string
busca = conteudo.find("teste")
print(busca)