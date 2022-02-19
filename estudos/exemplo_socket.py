from socket import *
import socket
resp = "S"
# while (resp == "S"):
#     url = input("Digite uma url: ")
#     ip = socket.gethostbyname(url)
#     print("O IP referente à url informada é: ", ip)
#     resp = input("Digite <s> para continuar: ").upper()

print("Domínio: ",socket.getservbyname("domain"))
print("HTTP: ",socket.getservbyname("http"))
print("FTP: ",socket.getservbyname("ftp"))

