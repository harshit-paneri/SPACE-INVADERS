from msilib.schema import Icon
from turtle import Screen
import pygame
import random

# init game
pygame.init()

# screen create
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('background.png')


# Title and icon
pygame.display.set_caption("SPACE INVADERS")
Icon = pygame.image.load('spaceshipgame.png')
pygame.display.set_icon(Icon)

# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40


# function player
def player(x, y):
    screen.blit(playerImg, (x, y))

# function enemy


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop
running = True
while running:

    #RGB (0,0,0)
    screen.fill((0, 0, 0))
    #background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke direction check
        if event.type == pygame.KEYDOWN:
            #print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 -0.1
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy boundry set
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

