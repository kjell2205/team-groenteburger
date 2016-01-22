import pygame, sys

pygame.init()

boardImage = pygame.image.load("./images/Board.png")

windowSize = boardImage.get_size()
screen = pygame.display.set_mode(windowSize)

boardImageSize = boardImage.get_size()

x, y = 0, 0

clock = pygame.time.Clock()

while 1:

    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    screen.blit(boardImage, (0, 0))

    pygame.display.update()
