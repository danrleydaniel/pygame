import pygame
import personagem
import objetos
from random import randint
from pygame.locals import *
'''
	Este projeto foi feito baseando-se na aula:
	https://www.youtube.com/watch?v=dFYjGvo9VKw

	Créditos dos sprites utilizados:
	Astronauta e plataforma: https://opengameart.org/content/astronaut-0
	Background: https://opengameart.org/content/parallax-space-scene-seamlessly-scrolls-too
	Alien inimigo: https://opengameart.org/content/alien-2d-sprites
	Nave espacial: https://opengameart.org/content/simple-spaceship (ainda não implementado)
	Gasolina: https://opengameart.org/content/sci-fi-goodscommodities
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
aleatoria = randint(50, 300) #Posição aleatória para a gasolina


'''   direita	  esquerda    parado   '''
pos = [[87, 116], [29, 58], [0, 145]] #Define a movimentação do astronauta

'''          pos1      pos2    pos3    dead      '''
pos_alien = [1    ,    93,     141,    45] #Define a movimentação do alien
'''         direita       esquerda      '''
pos_tiro = [   0   ,        33     ] #Define a movimentação do disparo

''' ÁREAS: '''
shoot_rect = pygame.Rect(13, 13, 13, 13) #Cria a área do disparo
gas_rect = pygame.Rect(0, 0, 19, 29) #Cria a área da gasolina
rocket_rect = pygame.Rect(52, 52, 52, 52) #Cria a área do foguete

''' SPRITES: '''
itens = pygame.image.load("images/astronauta.png") #Carrega os sprites do astronauta
fundo = pygame.image.load("images/background.jpg") #Carrega a imagem de fundo
alien = pygame.image.load("images/alienigena.png") #Carrega os sprites do alien
gas = pygame.image.load("images/gasolina.png") #Carrega o sprite da gasolina
shoot = pygame.image.load("images/disparo.png") #Carrega os sprites do tiro
rocket = pygame.image.load("images/foguete.png") #Carrega o sprite do foguete


''' PERSONAGENS CRIADOS: '''
astro = personagem.Personagem(0, 0, 200, 200, 29, 37) #Cria o astronauta
enemy = personagem.Alien(0, 0, 50, 200, 30, 37) #Cria o alien

''' OBJETOS CRIADOS: '''
gasosa = objetos.Gasolina(gas, aleatoria, 200, gas_rect) #Cria a gasolina
foguete = objetos.Foguete(rocket, 800, 190, rocket_rect) #Cria o foguete


''' GRUPOS: '''
shoots = pygame.sprite.Group() #Cria o grupo de disparos
grupo_gas = pygame.sprite.Group() #Cria o grupo de gasolina
rockets = pygame.sprite.Group() #Cria o grupo de foguetes

#Para tocar a música:
pygame.mixer.music.load("music/through space.ogg")
pygame.mixer.music.play()

def nothing_pressed():
	for i in pygame.key.get_pressed():
		if i == 1:
			return False

	return True

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

def draw_group(group): #Desenha um grupo
	for s in group:
		win.blit(s.image, (s.x, s.y))

def control(obj): #Controla o personagem
	global dire, mov
	key = pygame.key.get_pressed()
	if key[K_LEFT]:
		obj.x -= 1
		mov -= 1
		dire = 0
		obj.posicao = "left"
	if key[K_RIGHT] and obj.x < w - obj.w:
		obj.x += 1
		dire = 1
		mov += 1
		obj.posicao = "right"

	if nothing_pressed():
		if obj.posicao == "right":
			dire = 2
			mov = 0
		if obj.posicao == "left":
			dire = 2
			mov = 19

	if mov > 19:
		mov = 0
	if mov < 0:
		mov = 19



def is_colliding(obj1, obj2, dist): #Recebe os dois objetos que eu quero testar a colisão, e a distância de colisão desejada
	if obj1.x >= obj2.x - dist and obj1.x <= obj2.x + dist:
		return True

def hit(inimigo, disparo, dist): #Recebe como parâmetro o alien e o disparo, para ver se estão colidindo. Recebe também a distância de colisão
	if inimigo.x >= disparo.x and inimigo.x <= disparo.x + dist:
		return True

rockets.add(foguete)

while game:

	win.blit(fundo, (0,0)) #Coloca o background na tela

	control(astro) #Permite controlar o personagem
	if not astro.dentro_do_foguete: #Se o personagem não estiver dentro do foguete...
		masked_blit(win, itens, pos[dire][int(mov / 10)], astro.wy, astro.x, astro.y, astro.w, astro.h) #o jogo exibe na tela a animação do personagem
	masked_blit(win, alien, pos_alien[enemy.direc], enemy.wy, enemy.x, enemy.y, enemy.w, enemy.h) #Exibe na tela a animação do alien
	draw_group(shoots) #Desenha o grupo de disparos
	draw_group(grupo_gas) #Desenha o grupo de gasolinas
	draw_group(rockets) #Desenha o grupo de foguetes
	pygame.display.flip() #Atualiza a tela

	win.fill((255, 255, 255))

	if is_colliding(astro, enemy, 25): #Se o astronauta colidir com o inimigo...
		if enemy.vivo: #...se o alienígena estiver vivo...
			print("O alienígena te atacou!") #...o jogo diz que o alienígena atacou.

	if is_colliding(astro, foguete, 15): #Se o astronauta colidir com o foguete...
		if not astro.com_a_gasolina: #... e não estiver com a gasolina...
			print("Você precisa da gasolina para ligar o foguete") #... o jogo diz que ele precisa da gasolina para ligar o foguete...
		else: #... mas se estiver...
			astro.entrar_no_foguete() #... o astronauta entra no foguete.
			foguete.ligar()

	if gasosa.gerado: #Se a gasolina estiver gerada...
		if is_colliding(astro, gasosa, 25): #... e os astronauta estiver colidindo com ela...
			print("Você pegou a gasolina!") #... o jogo diz que o astronauta pegou a gasolina...
			astro.pegar_gasolina()
			gasosa.kill() #... destrói o sprite...
			gasosa.destruir() #... e destrói a gasolina gerada.

	for t in shoots:
		if t.rect.centerx > (astro.x + 1000):
			t.kill() #Se o tiro se afastar muito do personagem, ele é deletado
		if t.rect.centerx < (astro.x - 1000):
			t.kill() #Se o tiro se afastar muito do personagem, ele é deletado

		if hit(enemy, t, 20): #Quando o tiro atinge o inimigo...
			if enemy.vivo: #... se o alienígena estiver vivo...
				t.kill() #... o tiro é deletado...
				enemy.matar() #... o alienígena morre...
				gasosa.gerar() #... o tanque de gasolina é gerado...
				grupo_gas.add(gasosa) #... e é adicionado ao grupo.

	enemy.update(w) #Atualiza as animações do alien
	shoots.update() #Atualiza os tiros
	rockets.update() #Atualiza os foguetes
	relo.tick(700) #Dá uma pausa de 700 milissegundos no jogo para as animações não ficarem muito frenéticas

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			game = False #O jogo para quando o jogador aperta o X

		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE: #O personagem atira quando o jogador aperta espaço
				tiro = objetos.Tiro(dire, shoot, astro, shoot_rect)
				shoots.add(tiro)


'''
Desafios para as próximas atualizações:

	- Colocar alien inimigo (✓)
	- Adicionar colisão com inimigo (✓)
	- Adicionar disparos do astronauta(✓)
	- Adicionar sistema de gasolina e foguete (✓)
	- Adicionar múltiplas fases ()
	- Adicionar boss na fase 3 ()
	- Adicionar menu ()
	- Adicionar mensagem no final ()
'''
