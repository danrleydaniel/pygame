import pygame

''' Barulho da explosão criado por: Luke.RUSTLTD (https://opengameart.org/content/bombexplosion8bit)'''

def main():
	pygame.init()
	tela = pygame.display.set_mode([300, 300])
	pygame.display.set_caption("Iniciando com Pygame")
	relogio = pygame.time.Clock()
	cor_branca = (255,255,255)
	cor_azul = (108, 194, 236)
	cor_verde = (152, 231, 114)
	cor_vermelha = (227, 57, 9)
	cor_rosa = (253, 147, 226)
	sup = pygame.Surface((200, 200))
	sup.fill(cor_azul)

	sup2 = pygame.Surface((100, 100))
	sup2.fill(cor_verde)

	ret = pygame.Rect(10, 10, 45, 45)
	ret2 = pygame.Rect(50, 50, 80, 80)

	

	sair = False

	pygame.font.init()

	font_padrao = pygame.font.get_default_font()
	fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
	fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

	audio_explosao = pygame.mixer.Sound("8bit_bomb_explosion.wav")

	while sair != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.mouse.set_pos(150, 150)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ret.move_ip(-10, 0)

				if event.key == pygame.K_RIGHT:
					ret.move_ip(10, 0)

				if event.key == pygame.K_UP:
					ret.move_ip(0, -10)

				if event.key == pygame.K_DOWN:
					ret.move_ip(0, 10)

				if event.key == pygame.K_SPACE:
					ret.move_ip(10,10)

				if event.key == pygame.K_BACKSPACE:
					ret.move_ip(-10, -10)
		
		relogio.tick(30)
		tela.fill(cor_branca)
		tela.blit(sup, [50,50])
		tela.blit(sup2, [70,70])

		(xant, yant) = (ret.left, ret.top)
		(ret.left, ret.top) = pygame.mouse.get_pos()
		ret.left -= int(ret.width/2)
		ret.top -= int(ret.height/2) 
		if ret.colliderect(ret2):
			text = fonte_perdeu.render("COLIDIU", 1, (0,0,0))
			(ret.left, ret.top) = (xant, yant)
			audio_explosao.play()
			tela.blit(text, (150, 150))
		pygame.draw.rect(tela, cor_vermelha, ret)
		pygame.draw.rect(tela, cor_rosa, ret2)
		pygame.display.update()
	pygame.quit()

main()
