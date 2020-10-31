import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()

#Essa matriz representa a plataforma. Cada "." é um espaço vazio. Cada "P" é um espaço ocupado pelo piso.
matriz = [
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	"...PPPPP.........................................................................",
	".................................................................................",
	".......PPPPP.....................................................................",
	".................................................................................",
	"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
]



screen = pygame.display.set_mode((WIDTH, HEIGHT),0) #Pinta a plataforma
BLOCK_W = WIDTH // 16 # ---\ Esses valores representam o tamanho de cada
BLOCK_H = HEIGHT // 12 #---/ bloquinho.

caracteres = pygame.image.load("Sprite/Owlet_Monster_Attack1_4.png") #Carrega a imagem do personagem

#Classe que traz os atributos do protagonista
class Boy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		boy_original = caracteres.subsurface((32 * 0, 32 * 0), (32, 32)) #Recorta apenas o sprite que eu quero da imagem carregada na linha 30. Para entender melhor isso, é bom assistir: https://youtu.be/trOnGGsKtjg?t=1426
		self.image = pygame.transform.scale(boy_original, (BLOCK_W, BLOCK_H)) #Redimensionaliza o sprite, para que não fique muito pequeno
		self.rect = pygame.Rect((100, 100), (BLOCK_W, BLOCK_H))
		self.vel_x = 0
		self.vel_y = 0
		self.gravidade = 0.009

	def mover_esquerda(self):
		self.vel_x = -1 #Faz o personagem andar para a esquerda, diminuindo 1 do eixo X

	def mover_direita(self):
		self.vel_x = 1 #Faz o personagem andar para a direita, aumentando 1 no eixo X

	def pular(self):
		self.vel_y = -1 #Faz o personagem pular, diminuindo 1 no eixo Y

	def update(self, *args):
		self.vel_y += self.gravidade # A velocidade com a qual o personagem cai, aumentando valores no eixo Y, é definida pelo atributo gravidade
		self.rect.centerx += self.vel_x # Operação que faz o personagem ir para a direita ou esquerda
		self.rect.centery += self.vel_y # Operação que faz o personagem pular

	def parar_horizontal(self):
		self.vel_x = 0 #Quando o personagem não está indo nem para a direita, nem para a esquerda


boy = Boy() #Criando um objeto da classe Boy, que contém as informações do protagonista
herois = pygame.sprite.Group(boy) #Adiciona o protagonista a um grupo de sprites, conhecido como "heróis"

#Laço principal rotina do Pygame
while True:
	#Esse pinta os quadradinhos na plataforma conforme definido na matriz
	for linha, lin in enumerate(matriz):
		for coluna in range(0,16):
			x = coluna * BLOCK_W
			y = linha * BLOCK_H
			bloco = matriz[linha][coluna]
			cor = (0,0,0)
			if bloco == "P":
				cor = (255, 255, 0)
			pygame.draw.rect(screen, cor, ((x,y), (BLOCK_W, BLOCK_H)), 0)

	#Desenha o grupo de heróis, ao qual o protagonista faz parte
	herois.draw(screen)

	pygame.display.update()

	#Calcula regras
	herois.update()

	#Processa eventos
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()

		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT:
				boy.mover_direita() #O personagem vai para a direita, quando aperta-se a tecla da seta direita no teclado

			if e.key == pygame.K_LEFT:
				boy.mover_esquerda() #O personagem vai para a esquerda, quando aperta-se a tecla da seta esquerda no teclado

			if e.key == pygame.K_SPACE:
				boy.pular() #O personagem pula quando aperta-se o espaço no teclado

		if e.type == pygame.KEYUP:
			if e.key in [pygame.K_LEFT, pygame.K_RIGHT]:
				boy.parar_horizontal() #Quando nem a tecla da seta direita, nem da esquerda estão apertadas, o personagem para
