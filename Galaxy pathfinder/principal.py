import pygame
import personagem
from pygame.locals import *
'''
	Este projeto foi feito baseando-se na aula:
	https://www.youtube.com/watch?v=dFYjGvo9VKw

	Créditos dos sprites utilizados:
	Astronauta e plataforma: https://opengameart.org/content/astronaut-0
	Background: https://opengameart.org/content/parallax-space-scene-seamlessly-scrolls-too
	Alien inimigo: https://opengameart.org/content/alien-2d-sprites (ainda não implementado)
	Nave espacial: https://opengameart.org/content/simple-spaceship (ainda não implementado)
	Gasolina: https://opengameart.org/content/sci-fi-goodscommodities (ainda não implementado)
	Disparo e boss: https://opengameart.org/content/sci-fi-shoot-em-up-object-images (ainda não implementado)
	Música de fundo: https://opengameart.org/content/through-space (ainda não implementado)
'''


pygame.init()

w = 870
h = 370
win = pygame.display.set_mode((w, h))
game = True
dire = 0
mov = 0

'''   direita	  esquerda    parado   '''
pos = [[87, 116], [29, 58], [0, 145]]

itens = pygame.image.load("images/astronauta.png")
fundo = pygame.image.load("images/background.jpg")
astro = personagem.Personagem(0, 0, 200, 200, 29, 37)

def masked_blit(win, img, wx, wy, x, y, w, h):
	'''
		win -> janela do jogo
		img -> spritsheet
		wx -> posição na foto onde o sprite está localizado
		wy -> posição na foto onde o sprite está localizado (cima)
		w -> largura de cada sprite individual
		h -> altura de cada sprite individual
	'''
	surf = pygame.Surface((w, h)).convert()
	surf.blit(img, (0, 0), (wx, wy, w, h))
	alpha = surf.get_at((0, 0))
	surf.set_colorkey(alpha)
	win.blit(surf, (x, y))

def control(obj):
	global dire, mov
	key = pygame.key.get_pressed()
	if key[K_LEFT]:
		obj.x -= 1
		mov -= 1
		dire = 0
	if key[K_RIGHT] and obj.x < w - obj.w:
		obj.x += 1
		dire = 1
		mov += 1

	if mov > 19:
		mov = 0
	if mov < 0:
		mov = 19

while game:

	win.blit(fundo, (0,0))

	control(astro)
	masked_blit(win, itens, pos[dire][int(mov / 10)], astro.wy, astro.x, astro.y, astro.w, astro.h)
	pygame.display.flip()

	win.fill((255, 255, 255))

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			game = False

'''
Desafios para as próximas atualizações:

	- Colocar aliens inimigos ()
	- Adicionar colisão com inimigos ()
	- Adicionar disparos do astronauta()
	- Adicionar sistema de gasolina e foguete ()
	- Adicionar múltiplas fases ()
	- Adicionar boss na fase 3 ()
	- Adicionar menu ()
	- Adicionar mensagem no final ()
'''
