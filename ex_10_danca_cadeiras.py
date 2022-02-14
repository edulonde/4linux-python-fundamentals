from random import randint
import time

participantes = ['Grace', 'Ada', 'Neumann', 'Dijkstra', 'Guido']


def gerar_num_aleatorio():
    tam_ptcpts = len(participantes)
    num_aleatorio = randint(0, tam_ptcpts - 1)
    return num_aleatorio


def aguardar_03_segundos():
    time.sleep(2)


def principal():
    print("número de participantes da rodada: ",len(participantes))
    if len(participantes) > 1 :
        print(f"Que comece a rodada! Boa sorte aos participantes: \n"
              f"{participantes}")

        while len(participantes) != 1 :
            n_aleatorio = gerar_num_aleatorio()
            print(n_aleatorio)
            print(f"O candidato a sair foi: {participantes[n_aleatorio]}")
            del participantes[n_aleatorio]
            print('.' * 9)
            aguardar_03_segundos()

    print(f"O vencedor foi {participantes[0]}")


if __name__ == "__main__":
    principal()
