import numpy as np
from math import *
import pygame
import sys
from pygame.locals import*
import random as rd

v=8
pygame.init()


black=[0,0,0]
def mvt_ball(v,direction,angle,x,y):
    
    v=v+angle
    if direction:
        x+=v-angle
        y+=angle
    else:
        x-=v-angle
        y-=angle
    return x,y
def transforme_angle(angle):
    
    if angle<0:
        angle=abs(angle)
    else:
        angle=-1*angle
    return angle
def rebondit(v,angle,x,y):
    if y<0 or y>1000:
        angle=transforme_angle(angle)
    return angle


smash_cpt1=0
smash_cpt2=0
c_max_atteint=True
c=250 
r=0
g=0
b=0

blue=[0,0,250]
red=[250,0,0]
green=[0,250,0]
cpt_smash=0
tab1=[]
tab2=[]

direction=True
#droite
angle=rd.randint(-12,12)

smash=False
def raquette(ballx,bally,direction,x1,y1,x2,y2,angle,v):
    if direction:
       

        
        if ballx>x2-3 and ((bally<y2+130 and bally>y2+80) or (bally<y2+40 and bally>y2)):
            direction=False
            angle=transforme_angle(angle)
            v=7
        if ballx>x2-3 and bally<y2+80 and bally>y2+40:
            direction=False
            angle=transforme_angle(angle)
            v=rd.randint(7,18)
        if ballx>x2-3 and bally<y2+130 and bally>y2+90:
            angle-=4
        if ballx>x2-3 and bally<y2+40 and bally>y2:
            angle+=4

    else:
        if ballx<x1+35 and ((bally<y1+130 and bally>y1+80) or (bally<y1+40 and bally>y1)) :
            direction=True
            angle=transforme_angle(angle)
            v=7
        if ballx<x1+35 and bally<y1+80 and bally>y1+40:
            direction=True
            angle=transforme_angle(angle)
            v=rd.randint(7,18)
        if ballx<x1+25 and bally<y1+130 and bally>y1+90:
            angle+=4
        if ballx<x1+25 and bally<y1+40 and bally>y1:
            angle-=4
            
            
    return direction,angle,v

scorej1=0
scorej2=0
x_ball=700
y_ball=500
hx_ball=5
hy_ball=5

x1=0
y1=10
y2=0
x2=1390

hx1=0
hy1=0
hx2=0
hy2=0
white=[250,250,250]
redlight=[250,100,100]
bluelight=[100,100,250]
font=pygame.font.Font(None, 100)
score_j1 = font.render(str(scorej1),1,(blue))
score_j2 = font.render(str(scorej2),1,(red))
TXTSCORE= font.render(":",1,white)

black=[0,0,0]
running=True
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1400,1000))
fps=120
parti_en_cour=False
#main---------------------------------
cpt=0
while running:
    screen.fill(black)
    keys = pygame.key.get_pressed()
    clock.tick(fps)
    if parti_en_cour:
        

        if x_ball>1406:
            scorej1+=1
            font=pygame.font.Font(None, 100)
            score_j1 = font.render(str(scorej1),1,(blue))
            
            
            parti_en_cour=False

        if x_ball<-6:
            scorej2+=1
            font=pygame.font.Font(None, 100)
            score_j2 = font.render(str(scorej2),1,(red))
            parti_en_cour=False

        



        screen.fill(black)

        screen.blit(score_j1,(480,10))
        
        screen.blit(score_j2,(900,10))




        angle=rebondit(v,angle,x_ball,y_ball)
        
        

        
        if keys[pygame.K_z]:
            if y1>0:
                y1-=7
        if keys[pygame.K_s]:
            if y1<890:
                y1+=7
        if keys[pygame.K_UP]:
            if y2>0:
                y2-=7
        if keys[pygame.K_DOWN]:
            if y2<890:
                y2+=7
        x_ball,y_ball=mvt_ball(v,direction,angle,x_ball,y_ball)
        direction,angle,v=raquette(x_ball,y_ball,direction,x1,y1,x2,y2,angle,v)
        
        pygame.draw.rect(screen,white,(695,0,10,1000))
        pygame.draw.circle(screen, white, (x_ball,y_ball), 10, 10)
        pygame.draw.rect(screen,bluelight,(x1,y1,10,120))
        pygame.draw.rect(screen,redlight,(x2,y2,10,120))
        pygame.draw.rect(screen,blue,(x1,y1+40,10,40))
        pygame.draw.rect(screen,red,(x2,y2+40,10,40))
        
        #faut que ca attende et une fois que ca a attendu ca l'affiche NAN FAUT LE CALCULER AVEC LANGLE OU AVEC UN CPT
       
        pygame.display.flip()
    else:
        x1=0
        y1=450
        y2=450
        x2=1390
        if keys[pygame.K_SPACE]:
            parti_en_cour=True 
            if direction:
                x_ball=100
                y_ball=500
            else:
                x_ball=1300
                y_ball=500
            v=7

            angle=rd.randint(-12,12)
            tps0=pygame.time.get_ticks()


        
        if c>230:
            c_max_atteint=True 
        elif c<20:
            c_max_atteint=False
        if  c_max_atteint ==False:
            c+=6

        elif c_max_atteint:
            c-=6
        
        blancnoir = [c,c,c]

        font=pygame.font.Font(None, 150)
        REJOUER= font.render("SPACE = REJOUER",1,blancnoir)

        screen.blit(score_j1,(480,10))
        screen.blit(TXTSCORE,(700,10))
        screen.blit(score_j2,(900,10))
        screen.blit(REJOUER,(250,500))
        pygame.display.flip()






    
    for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
    
