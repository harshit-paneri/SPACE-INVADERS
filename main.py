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

def player():
    screen.blit(playerImg ,(playerX, playerY))

#Game loop
running = True
while running:
    
    #RGB (0,0,0)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    player()
    pygame.display.update()