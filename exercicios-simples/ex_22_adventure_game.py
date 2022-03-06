from time import sleep
import pygame

pygame.mixer.init()
pygame.mixer.music.load('typewriter-2.ogg')

def maquina_de_escrever(texto):
    pygame.mixer.music.play()
    for caracter in texto:
        print(caracter, end="", flush=True)
        sleep(0.035)

texto = "Você acordou em um labirinto misterioso, oque você deseja fazer? \n"

while True:
    maquina_de_escrever(texto)
    opcao = input(f'1 - explorar o lugar\n'
                  f'2 - pegar algum objeto do lugar\n'
                  f'3 - pegar algum objeto da mochila\n'
                  f'4 - sair do jogo\n')