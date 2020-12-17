import pygame

def main():
	pygame.init()
	tela = pygame.display.set_mode([300, 300])
	pygame.display.set_caption("Iniciando com Pygame")
	relogio = pygame.time.Clock()
	cor_branca = (255,255,255)
	sup = pygame.Surface((200, 200))

	sair = False

	while sair != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True
		relogio.tick(27)
		tela.fill(cor_branca)
		tela.blit(sup, [10,10])
		pygame.display.update()
	pygame.quit()

main()
