import pygame
from pygame.locals import *
import random

pygame.init()

# TELA
tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Jogo da Cobrinha')

#Cores
vermelho = (255, 0, 0)

#Direções ad cobrinha
left = K_LEFT
right = K_RIGHT
up = K_UP
down = K_DOWN

passo = 10

#cobrinha
cobrinha_pos = [(300, 300)]
cobrinha_sup = pygame.Surface((10, 10))
cobrinha_sup.fill((0, 255, 0))
cobrinha_dir = down

#maca_rng
def gerar_posicao_maca():
    while True:
        nova_posicao = (random.randint(0, (tamanho_tela[0] // 10) - 1) * 10, random.randint(0, (tamanho_tela[1] // 10) - 1) * 10)
        if nova_posicao not in cobrinha_pos:
            return nova_posicao

maca_pos = gerar_posicao_maca()

while True:
    tela.fill((0, 0, 0))  # Limpa a tela

    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key in [left, right, up, down]:
                cobrinha_dir = event.key

    if cobrinha_dir == left:
        nova_posicao = (cobrinha_pos[0][0] - passo, cobrinha_pos[0][1])
    if cobrinha_dir == right:
        nova_posicao = (cobrinha_pos[0][0] + passo, cobrinha_pos[0][1])
    if cobrinha_dir == up:
        nova_posicao = (cobrinha_pos[0][0], cobrinha_pos[0][1] - passo)
    if cobrinha_dir == down:
        nova_posicao = (cobrinha_pos[0][0], cobrinha_pos[0][1] + passo)
    
    cobrinha_pos.insert(0, nova_posicao)

    for pos in cobrinha_pos:
        tela.blit(cobrinha_sup, pos)

    if cobrinha_pos[0] == maca_pos:
        maca_pos = gerar_posicao_maca()
    else:
        cobrinha_pos.pop()

    #comidinha :)
    apple_size = pygame.Surface((10, 10))
    apple_size.fill(vermelho)
    tela.blit(apple_size, maca_pos)
    pygame.display.update()  # Atualiza a tela