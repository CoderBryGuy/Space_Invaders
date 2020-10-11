import pygame
from pygame import mixer
import random
import math

# initialize pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# title and icon
icon = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/ufo .png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")

# background
background = pygame.image.load("/home/bryan/IdeaProjects/Python/Space_Invaders/background1.png")

# background sound
mixer.music.load('/home/bryan/IdeaProjects/Python/Space_Invaders/game_music.wav')
mixer.music.play(-1)

# create screen
screen = pygame.display.set_mode((800, 600))

# player
playerImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/space-invaders.png')
playerX = 370
playerY = 480
playerX_velocity = 0
playerY_velocity = 0

# # enemy
# enemyImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/enemy_alien.png')
# enemyX = random.randint(0, 736)
# enemyY = random.randint(50, 150)
# enemy_x_velocity = 2
# enemy_y_velocity = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemy_x_velocity = []
enemy_y_velocity = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/enemy_alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemy_x_velocity.append(2)
    enemy_y_velocity.append(0)

# bullet
bulletImg = pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/bullet.png')
bulletX = playerX
bulletY = playerY
bullet_x_velocity = 0
bullet_y_velocity = 7
# bullet_state = "ready"
bullet_is_firing = False

# explosion
explosionImg = []
explosionX = []
explosionY = []
explosion_countDown = []
num_of_potential_explosions = num_of_enemies

for i in range(num_of_potential_explosions):
    explosionImg.append(pygame.image.load('/home/bryan/IdeaProjects/Python/Space_Invaders/explosion.png'))
    explosionX.append(0)
    explosionY.append(0)
    explosion_countDown.append(0)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def clamp(val, max, min):
    if val >= max:
        val = max
        return val
    elif val <= min:
        val = min
        return val
    else:
        return val


def alternate_enemy_velocity(en_x, en_vel_x, max_x, min_x, i):
    global enemyY
    y_change = 40
    if en_x >= max_x:
        en_vel_x = en_vel_x * -1
        enemyY[i] = enemyY[i] + y_change
        enemyY[i] = clamp(enemyY[i], 600, 0)
        return en_vel_x
    elif en_x <= min_x:
        en_vel_x = en_vel_x * -1
        enemyY[i] = enemyY[i] + y_change
        enemyY[i] = clamp(enemyY[i], 600, 0)
        return en_vel_x
    else:
        return en_vel_x


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


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet(x, y):
    screen.blit(bulletImg, (x, y))


def fire_bullet(x, y):
    global bullet_is_firing
    bullet_is_firing = True
    screen.blit(bulletImg, (x + 16, y + 10))


def init_explosion(x, y, j):
    global explosionX
    global explosionY
    global explosion_countDown

    explosionX[j] = x
    explosionY[j] = y
    explosion_countDown[j] = 50


def print_explosion(j):
    global explosionImg
    global explosionX
    global explosionY

    screen.blit(explosionImg[j], (explosionX[j], explosionY[j]))


def is_collision(enX, enY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enX - bulletX, 2)) + (math.pow(enY - bulletY, 2)))

    if distance < 27:
        return True
    else:
        return False


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
                    bullet_sound = mixer.Sound('/home/bryan/IdeaProjects/Python/Space_Invaders/laser_fire.wav')
                    bullet_sound.play()
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

    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemy_x_velocity[i] = alternate_enemy_velocity(enemyX[i], enemy_x_velocity[i], 736, 0, i)
        enemyX[i] += enemy_x_velocity[i]

        # collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('/home/bryan/IdeaProjects/Python/Space_Invaders/enemy_hit.wav')
            collision_sound.play()
            bulletY = 480
            # bullet_state = "ready"
            bullet_is_firing = False
            score_value += 1
            print(score_value)

            init_explosion(enemyX[i], enemyY[i], i)

            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        for k in range(num_of_potential_explosions):
            if explosion_countDown[k] > 0:
                explosion_countDown[k] -= 1
                print_explosion(k)

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
    show_score(textX, textY)
    pygame.display.update()
