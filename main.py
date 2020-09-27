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
playerX_velocity = 0
playerY_velocity = 0


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


running = True

# game loop
while running:
    # RGB red, green, blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke pressed check if left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_velocity = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_velocity = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_velocity = 0

    playerX += playerX_velocity
    player(playerX, playerY)
    pygame.display.update()
