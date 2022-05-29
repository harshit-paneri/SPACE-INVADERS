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


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False