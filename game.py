import pygame, sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Buy a ride", 1, (255, 0, 255), (255, 255, 255))

helloWorldize = helloWorld.get_size()

x, y = 0, 0
directionX = 5
directionY = 5

clock = pygame.time.Clock()

while 1:

    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if x + helloWorldize[0] > windowSize[0] or x < 0:
        directionX *= -1

    if y + helloWorldize[1] > windowSize[1] or y < 0:
        directionY *= -1

    screen.fill((0, 0, 0))

    screen.blit(helloWorld, (x, y))

    x += directionX
    y += directionY

    pygame.display.update()