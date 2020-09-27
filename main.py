import pygame

# initialize pygame
pygame.init()

# title and icon
icon = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/ufo .png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")

# create screen
screen = pygame.display.set_mode((800, 600))

# player
playerImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/space-invaders.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


running = True

# game loop
while running:
    # RGB red, green, blue
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
