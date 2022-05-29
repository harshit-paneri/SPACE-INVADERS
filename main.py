from msilib.schema import Icon
from turtle import Screen
import pygame

#init game  
pygame.init()

#screen create
screen = pygame.display.set_mode((800, 600))


# Title and icon
pygame.display.set_caption("SPACE INVADERS")
Icon = pygame.image.load('spaceshipgame.png')
pygame.display.set_icon(Icon)

#player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# function player
def player(x,y):
    screen.blit(playerImg ,(x, y))

#Game loop
running = True
while running:
    
    #RGB (0,0,0)
    screen.fill((0,0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke direction check
        if event.type == pygame.KEYDOWN:
            #print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 -0.1
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()