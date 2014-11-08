import pygame
import random
import time
from ipdb import set_trace

pygame.init()



def mainloop():
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    size_x=600
    size_y=400
    offsetx=50
    offsety=50
    size=[size_x+offsetx*2,size_y+offsety*2]
    screen=pygame.display.set_mode(size)


    g=9.81/5
    dt=0.05
    vy=0
    vx=6
    x=0
    y=0
    height=200
    bounce=-10
    pipedistance=120
    pipewidth=50
    pipegap=120
    pipes=[]
    birdsize=5
    prev = None

    for i in range((size_x/pipedistance)):
        j=i+1
        bottom_edge=random.randint(0,size_y-pipegap)
        left_edge=j*pipedistance-(pipewidth/2)
        top_edge=bottom_edge+pipegap
        right_edge=left_edge+pipewidth
        pipes+=[(bottom_edge,top_edge,left_edge,right_edge)]

    label=None
    font=pygame.font.Font(None, 30)

    screen.fill(white)
    window=pygame.Surface((size_x,size_y))
    bg=pygame.Surface((size_x,size_y))
    bg.fill(white)
    pygame.draw.rect(bg, red, (0,0,size_x,size_y), 3)
    moving = True
    control = True
    bg.fill(white)
    pygame.draw.rect(bg, red, (0,0,size_x,size_y), 3)

    for i in pipes:
        pygame.draw.rect(bg,black,[i[2],i[1],pipewidth,size_y-i[1]])
        pygame.draw.rect(bg,black,[i[2],0,pipewidth,i[0]])
    
    bird=pygame.Surface((birdsize*2,birdsize*2), pygame.SRCALPHA)
    bird.fill( (255,255,255,0) )
    pygame.draw.circle(bird,red,[birdsize,birdsize],birdsize)

    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                #set_trace()
                if event.key == 27: #esc
                    return False
                if event.unicode == ' ' and control:
                    vy = bounce
                if event.unicode == 'r':
                    return True

        if moving: 
            x += dt*vx
            y += dt*vy
            vy += g*dt

        if x>=size_x or x<=0 or y>=size_y:
            moving = False
            vx = 0
            vy = 0


        #generating pipes
        #tuple in pipes: (bottom_edge,top_edge,left_edge,right_edge)
        for i in pipes:
            if i[2]<x<i[3] and (i[1]<y<size_y or 0<y<i[0]):
                control = False

        window.blit(bg,(0,0))
        window.blit(bird,(x-birdsize,y-birdsize))
        screen.blit(window,(offsetx,offsety))
        
        pygame.display.flip()
        cur = time.time()
        if prev:
            delay = 1.0/100 - (cur-prev)
            if delay > 0:
                time.sleep(delay)

        prev = time.time()


def game():
    while mainloop():
        pass
    
    pygame.quit()

def main():
    game()

if __name__ == "__main__":
    main()
