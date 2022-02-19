import serial
conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("/dev/ttyUSB"+str(porta), 9600)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    while True:
        resposta = conexao.read()
        if resposta=='1':
            print("LED Ligado")
        else:
            print("LED Desligado")
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")