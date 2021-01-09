import pygame

pygame.init()

'''

	ARTES DO JOGO FEITAS POR:
	surt

	Site:
	https://opengameart.org/content/monkey-lad-in-magical-planet

'''

tela = pygame.display.set_mode((800, 400),0)
sprites = pygame.image.load("sprites/monkeylad_further.png").convert_alpha()

matriz = [
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"................................................................................",
"...........................................................PPPP.................",
".......................PPPP.........................PPPP........................",
"................................................................................",
"..................................PPPP..........................................",
"................................................................................",
"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]

jogar = True

def get_image_by_gid(spritesheet, gid, columns = 64, w=16, h=16, spc_h=0, spc_v=0, margin_left=0, margin_top=0):
	linha = gid // columns
	coluna =  gid % columns
	x = margin_left + (coluna * (w + spc_h))
	y = margin_top + (linha * (h + spc_v))
	return spritesheet.subsurface((x , y) , (w , h))


def pintar_cenario():
	img = get_image_by_gid(sprites, 7)
	tela.blit(img, (100, 100))

while jogar:

	#calcular as regras

	#pintar a tela
	pintar_cenario()
	pygame.display.update()

	#captura os eventos
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			jogar = False
