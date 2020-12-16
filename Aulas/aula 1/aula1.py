import pygame

def main():
	pygame.init()
	pygame.display.set_mode([300, 300])
	pygame.display.set_caption("Iniciando com Pygame")
	sair = False

	while sair != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True

	pygame.display.update()
	pygame.quit()

main()
