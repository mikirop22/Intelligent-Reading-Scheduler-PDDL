import pygame

screen = pygame.display.set_mode([1000,750])
clock = pygame.time.Clock()
score = 0

done = False

background = pygame.image.load("background.jpg").convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()