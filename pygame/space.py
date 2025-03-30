import pygame
from pygame import mixer

pygame.init()#Intialize

screen=pygame.display.set_mode((600,500))#create screen

background=pygame.image.load('game.jpg')#background image

enemy=pygame.image.load('image.png')#enemy

a=1
running=True
while running:
    
    screen.fill((0,0,0))
    
    screen.blit(background,(0,0))
    
    screen.blit(enemy,(a,10))
    a+=1
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    pygame.display.update()

pygame.quit()
