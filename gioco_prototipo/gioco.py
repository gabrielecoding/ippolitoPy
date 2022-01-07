import pygame
from pygame.locals import *
import random
import os

from pygame.constants import K_0, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, K_a, K_d, K_s, K_w
from pygame.time import Clock

os.chdir ("/Users/gabriele/Downloads/immagini")

pygame.init()
random.seed()

all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

sfondo = pygame.image.load("sfondo.png")
uccello = pygame.image.load("uccello.png")
base = pygame.image.load("base.png")
game_over = pygame.image.load("gameover.png")



clk = pygame.time.Clock()



#Costanti globali
SCHERMO = pygame.display.set_mode((512,288))
FPS = 50
VEL_AVANZ = 3



def inizializza():
    
    global all_sprites, all_enemies, set_timer, clock, firerate
    global uccellox, uccelloy, uccello_vely, uccello_volo
    global basex
    global pro_x, pro_y, lancio, nemico, rimuovi, allsprites, allenemies
    uccellox, uccelloy = 60,150
    uccello_vely = 0
    uccello_volo = 2
    basex = 0
    pro_x=500
    lancio = False
    nemico = False
    rimuovi = False
    allsprites= "vuoto"
    allenemies = "vuoto"
    all_sprites.empty()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = 0
    firerate = 0
    


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(base, (basex,270))
    SCHERMO.blit(uccello, (uccellox,uccelloy))
    if allsprites == "vuoto":
        all_sprites.empty()
        pass
    else:
        all_sprites.draw(SCHERMO)

    if allsprites == "vuoto":
        all_enemies.empty()
        pass
    else:
        all_enemies.draw(SCHERMO)

                    
    
    


def hai_perso():
    SCHERMO.blit(game_over, (50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()

#inizializzo Variabili
inizializza()
### Ciclo Principale ###


while True:
    basex -= VEL_AVANZ
    if basex < -2045: basex = 0
    keys=pygame.key.get_pressed()
    
    if keys[K_UP] or keys[K_w]:
        if uccelloy > 0:
            uccelloy -= 7
    else:
        if uccelloy < 250:
            uccelloy += 3
    if keys[K_DOWN] or keys[K_s]:
        if uccelloy < 250:
            uccelloy += 7
    if keys[K_RIGHT] or keys[K_d]:
        if uccellox < 472:
            uccellox += 7
    if keys[K_LEFT] or keys[K_a]:
        if uccellox > 0:
            uccellox -= 7

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

            
            spr_proiettile = pygame.sprite.Sprite(all_sprites)
            spr_proiettile.image = pygame.image.load("proiettile.png")
            spr_proiettile.rect = spr_proiettile.image.get_rect()

            spr_proiettile.rect.topright = (uccellox, uccelloy)
            lancio = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                inizializza()
        
        if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.USEREVENT: 
            clock += 1
            if clock == 10:
                clock= 0
                nemico = True
                spr_ghost = pygame.sprite.Sprite(all_enemies)
                spr_ghost.image = pygame.image.load("uccello.png")
                spr_ghost.rect = spr_ghost.image.get_rect()
                
                spr_ghost.rect.topright= (SCHERMO.get_width()-30, random.randrange(0, 288))
                
    if nemico == True:
        if spr_proiettile.rect == spr_ghost.rect:
                allghost = "vuoto"
        else :
            allghost= "pieno"
    
    if lancio == True:
        if spr_proiettile.rect.x < SCHERMO.get_width()-10:
            allsprites = "pieno"
            spr_proiettile.rect.x += 30
            
        else:
            allsprites = "vuoto"


        
        
    


    
    disegna_oggetti()
    aggiorna()