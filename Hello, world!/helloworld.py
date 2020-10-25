import pygame

background_image_filename = "underwater-photo-pool_1219-17.jpg"
mouse_image_filename = "0_jkQ6RhKtfGJ7xFbr_.png"


pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("Hello, world!")

background = pygame.image.load(background_image_filename)
mouse_cursor = pygame.image.load(mouse_image_filename)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.blit(background,(0,0))

	x, y = pygame.mouse.get_pos()
	x -= mouse_cursor.get_width()
	y -= mouse_cursor.get_height()
	screen.blit(mouse_cursor, (x,y))

	pygame.display.update()
