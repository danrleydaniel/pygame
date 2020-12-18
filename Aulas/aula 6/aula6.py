import pygame

def main():
	pygame.init()
	tela = pygame.display.set_mode([300, 300])
	pygame.display.set_caption("Iniciando com Pygame")
	relogio = pygame.time.Clock()
	cor_branca = (255,255,255)
	cor_azul = (108, 194, 236)
	cor_verde = (152, 231, 114)
	cor_vermelha = (227, 57, 9)
	sup = pygame.Surface((200, 200))
	sup.fill(cor_azul)

	sup2 = pygame.Surface((100, 100))
	sup2.fill(cor_verde)

	ret = pygame.Rect(10, 10, 45, 45)

	sair = False

	while sair != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				ret = ret.move(10, 10)
		relogio.tick(27)
		tela.fill(cor_branca)
		tela.blit(sup, [50,50])
		tela.blit(sup2, [70,70])
		pygame.draw.rect(tela, cor_vermelha, ret)
		pygame.display.update()
	pygame.quit()

main()
