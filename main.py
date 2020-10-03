import pygame
import random

# initialize pygame
pygame.init()

# title and icon
icon = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/ufo .png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")

# background
background = pygame.image.load("/home/bryan/IdeaProjects/Python/Space_Invaders/background1.png")

# create screen
screen = pygame.display.set_mode((800, 600))

# player
playerImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/space-invaders.png')
playerX = 370
playerY = 480
playerX_velocity = 0
playerY_velocity = 0

# enemy
enemyImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/enemy_alien.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemy_x_velocity = 2
enemy_y_velocity = 0

# bullet
bulletImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/bullet.png')
bulletX = playerX
bulletY = playerY
bullet_x_velocity = 0
bullet_y_velocity = 5
# bullet_state = "ready"
bullet_is_firing = False


# bullet_x_locked = False


def clamp(val, max, min):
    if val >= max:
        val = max
        return val
    elif val <= min:
        val = min
        return val
    else:
        return val


def alternate_enemy_velocity(enemy_x, vel_x, max_x, min_x):
    global enemyY
    y_change = 10
    if enemy_x >= max_x:
        vel_x = vel_x * -1
        enemyY = enemyY + y_change
        enemyY = clamp(enemyY, 200, 0)
        return vel_x
    elif enemy_x <= min_x:
        vel_x = vel_x * -1
        enemyY = enemyY + y_change
        enemyY = clamp(enemyY, 200, 0)
        return vel_x
    else:
        return vel_x


def check_enemy_coordinates(enemyX, enemyY, velX, velY):
    print("enemy X velocity : " + str(velX))
    print("enemy Y velocity : " + str(velY))
    print("enemy X position : " + str(enemyX))
    print("enemy Y position : " + str(enemyY))


def check_bullet_coordinates(bulX, bulY, velX, velY):
    print("bullet X velocity : " + str(velX))
    print("bullet Y velocity : " + str(velY))
    print("bullet X position : " + str(bulX))
    print("bullet Y position : " + str(bulY))


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


def bullet(x, y):
    screen.blit(bulletImg, (x, y))


def fire_bullet(x, y):
    global bullet_is_firing
    bullet_is_firing = True
    screen.blit(bulletImg, (x + 16, y + 10))


running = True

# game loop
while running:

    # RGB red, green, blue
    screen.fill((0, 0, 0))

    # add background img
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke pressed check if left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_velocity = -5
            if event.key == pygame.K_RIGHT:
                playerX_velocity = 5
            if event.key == pygame.K_SPACE:
                if not bullet_is_firing:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # if keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_velocity = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_velocity = 0

    playerY += playerY_velocity
    playerY = clamp(playerY, 536, 0)
    playerX += playerX_velocity
    playerX = clamp(playerX, 736, 0)
    player(playerX, playerY)

    enemy_x_velocity = alternate_enemy_velocity(enemyX, enemy_x_velocity, 736, 0)
    enemyX += enemy_x_velocity

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_is_firing = False
    if bullet_is_firing:
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_y_velocity

    # check various coordinates at give intervals
    # if count > 50:
    #     count = 0
    #     # check_enemy_coordinates(enemyX, enemyY, enemy_x_velocity, enemy_y_velocity)

    enemy(enemyX, enemyY)

    pygame.display.update()
