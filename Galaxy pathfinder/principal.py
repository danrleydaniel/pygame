import pygame
import personagem
from pygame.locals import *
'''
	Este projeto foi feito baseando-se na aula:
	https://www.youtube.com/watch?v=dFYjGvo9VKw

	Créditos dos sprites utilizados:
	Astronauta e plataforma: https://opengameart.org/content/astronaut-0
	Background: https://opengameart.org/content/parallax-space-scene-seamlessly-scrolls-too
	Alien inimigo: https://opengameart.org/content/alien-2d-sprites
	Nave espacial: https://opengameart.org/content/simple-spaceship (ainda não implementado)
	Gasolina: https://opengameart.org/content/sci-fi-goodscommodities (ainda não implementado)
	Disparo e boss: https://opengameart.org/content/sci-fi-shoot-em-up-object-images (ainda não implementado)
	Música de fundo: https://opengameart.org/content/through-space
'''


pygame.init()

#Variáveis globais:
w = 870 #Largura da tela
h = 370 #Altura da tela
win = pygame.display.set_mode((w, h)) #Criação da janela
game = True #Variável que diz se o game está rolando ou não
dire = 0 #Usado na movimentação do astronauta
mov = 0 #Usado na movimentação do astronauta
relo = pygame.time.Clock() #Relógio para diminuir um pouco a velocidade do jogo

'''   direita	  esquerda    parado   '''
pos = [[87, 116], [29, 58], [0, 145]] #Define a movimentação do astronauta

'''          pos1      pos2    pos3    '''
pos_alien = [1    ,    93,     141] #Define a movimentação do alien

itens = pygame.image.load("images/astronauta.png") #Carrega os sprites do astronauta
fundo = pygame.image.load("images/background.jpg") #Carrega a imagem de fundo
alien = pygame.image.load("images/alien.png") #Carrega os sprites do alien
astro = personagem.Personagem(0, 0, 200, 200, 29, 37) #Cria o astronauta
enemy = personagem.Alien(0, 0, 100, 200, 30, 37) #Cria o alien

#Para tocar a música:
pygame.mixer.music.load("music/through space.ogg")
pygame.mixer.music.play()

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

def is_colliding(obj1, obj2, dist): #Recebe os dois objetos que eu quero testar a colisão, e a distância de colisão desejada
	if obj1.x >= obj2.x - dist and obj1.x <= obj2.x + dist:
		return True

while game:

	win.blit(fundo, (0,0))

	control(astro)
	masked_blit(win, itens, pos[dire][int(mov / 10)], astro.wy, astro.x, astro.y, astro.w, astro.h)
	masked_blit(win, alien, pos_alien[enemy.direc], enemy.wy, enemy.x, enemy.y, enemy.w, enemy.h)
	pygame.display.flip()

	win.fill((255, 255, 255))

	if is_colliding(astro, enemy, 25):
		print("Está colidindo")

	enemy.update(w)
	relo.tick(700)

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			game = False

'''
Desafios para as próximas atualizações:

	- Colocar alien inimigo (✓)
	- Adicionar colisão com inimigo (✓)
	- Adicionar disparos do astronauta()
	- Adicionar sistema de gasolina e foguete ()
	- Adicionar múltiplas fases ()
	- Adicionar boss na fase 3 ()
	- Adicionar menu ()
	- Adicionar mensagem no final ()
'''
