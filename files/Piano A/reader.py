import pygame
from pygame.locals import *
from pygame import mixer
from time import sleep
#Initialisation
pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = mixer.music.load("a.mp3")
 
continuer = 1 #Variable de boucle
joue = 0 #1 si le son a été mis en pause
i=0
while continuer:
    for event in pygame.event.get():
        #Lancer le son
        if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
            while continuer:
                pygame.mixer.music.play()
                print("play")
                pygame.mixer.music.queue("a.mp3") 
                #joue = 1
                pygame.time.Clock().tick(30)
                #for b in range(10):
                #    print(b)
                if event.type == QUIT:
                    continuer = 0
                if i==5:
                    continuer=0
                else:
                    i+=1
                sleep(0.5)
                sleep(0.5)
        if event.type == KEYDOWN and event.key == K_RETURN:
            joue = 0

# if game started or back to main menu
#  pygame.mixer.music.unload
