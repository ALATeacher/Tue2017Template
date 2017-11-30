'''
@author: ALATeacher
Description: 
'''
import pygame
import sys, os, math
from pygame import *
from random import randint
from spriteHelper import SpriteSheet

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GAMENAME = "Awesome Game"
FRAMERATE = 60
BGCOLOR = (255,255,255)

class Player:
    '''The class used to identify the single player'''
    ##########VARIABLES##########
    x = 0
    y = 0
    vX = 0
    vY = 0
    collider = None
    
    ##########CONSTRUCTOR##########
    def __init__(self):
        self.image = SpriteSheet("p2_front.png")
        self.image = self.image.get_image(0,0,66,92)
    
    def draw(self,surface):
        '''draws the sprite for the player on the screen'''
        surface.blit(self.image,(self.x,self.y))
    
    def getCollider(self):
        '''returns a rectangle area representing the player sprite'''
        pass
    def getCenter(self):
        rect = self.image.get_rect()
        print(rect.x,rect.y)
        return (rect.w/2,rect.h/2)
    def process(self,delta):
        self.x += self.vX*delta
        self.vY += .002*delta
        self.y += self.vY*delta     

class Game:
    ##########VARIABLES##########
    score = 0
    levels = []
    player = None
    
    ##########CONSTRUCTOR##########
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption(GAMENAME)
        self.player = Player()
    
    #########MAIN FUNCTION##########
    def main(self):
        playing = True
        centerOfScreen = self.getCenterOfScreen()
        centerOfPlayer = self.player.getCenter()
        self.player.x = centerOfScreen[0]-centerOfPlayer[0]
        self.player.y = centerOfScreen[1]-centerOfPlayer[1]
        
        ##########GAME LOOP##########
        while playing:
            delta = self.clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        #JUMP
                        self.player.vY=-1
            self.processLogic(delta)
            self.drawScreen()
            pygame.display.flip()
                    
    def quit(self):
        pygame.quit()
        sys.exit()
        
    def processLogic(self,delta):
        self.player.process(delta)
    
    def drawScreen(self):
        self.surface.fill(BGCOLOR)
        
        self.player.draw(self.surface)
    
    def getCenterOfScreen(self):
        return (WINDOWWIDTH/2,WINDOWHEIGHT/2)
        
        
if __name__=='__main__':
    game = Game()
    game.main()
