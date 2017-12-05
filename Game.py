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

class Platform:
    '''The class used to identify individual platform blocks'''
    ##########VARIABLES##########
    x = 0
    y = 0
    image = None
    collider = None
    
    ##########CONSTRUCTOR##########
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
        self.collider = self.image.get_rect()
        self.collider.x = self.x
        self.collider.y = self.y
    
    def draw(self,surface):
        '''draws the sprite for the player on the screen'''
        surface.blit(self.image,(self.x,self.y))

class Player:
    '''The class used to identify the single player'''
    ##########VARIABLES##########
    x = 0
    y = 0
    vX = 0
    vY = 0
    collider = None
    isFalling = True
    speed = .3
    jumping = False
    
    ##########CONSTRUCTOR##########
    def __init__(self):
        self.image = SpriteSheet("p2_front.png")
        self.image = self.image.get_image(0,0,66,92)
    
    def draw(self,surface):
        '''draws the sprite for the player on the screen'''
        surface.blit(self.image,(self.x,self.y))
    
    def getCollider(self):
        '''returns a rectangle area representing the player sprite'''
        self.collider = self.image.get_rect()
        self.collider.x = self.x
        self.collider.y = self.y
        return self.collider
    
    def getCenter(self):
        rect = self.image.get_rect()
        print(rect.x,rect.y)
        return (rect.w/2,rect.h/2)
    
    def process(self,delta):
        if self.isFalling:
            self.x += self.vX*delta
            self.vY += .002*delta
            self.y += self.vY*delta     
    
    def move(self,direction,delta):
        self.x+=(direction*self.speed*delta)

class Game:
    ##########VARIABLES##########
    score = 0
    levels = []
    player = None
    platform = []
    
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
        grassLeftImage = SpriteSheet("grassLeft.png").get_image(0,0,70,70)
        grassMidImage = SpriteSheet("grassMid.png").get_image(0,0,70,70)
        grassRightImage = SpriteSheet("grassRight.png").get_image(0,0,70,70)
        platform1X = self.player.x
        platform1Y = self.player.y+self.player.image.get_rect().height
        platform1 = Platform(platform1X,platform1Y,grassMidImage)
        self.platform.append(platform1)
        
        platform1X = self.player.x+70
        platform1Y = self.player.y+self.player.image.get_rect().height
        platform2 = Platform(platform1X,platform1Y,grassRightImage)
        self.platform.append(platform2)
        
        platform1X = self.player.x-70
        platform1Y = self.player.y+self.player.image.get_rect().height
        platform2 = Platform(platform1X,platform1Y,grassLeftImage)
        self.platform.append(platform2)
        ##########GAME LOOP##########
        while playing:
            delta = self.clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        #JUMP
                        if not self.player.jumping:
                            self.player.vY=-1
                            self.player.jumping = True
            keys=pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.player.move(-1,delta)
            elif keys[K_RIGHT]:
                self.player.move(1,delta)
            self.processLogic(delta)
            self.drawScreen()
            pygame.display.flip()
                    
    def quit(self):
        pygame.quit()
        sys.exit()
        
    def processLogic(self,delta):
        self.player.process(delta)
        for platform in self.platform:
            c = platform.collider
            if self.player.getCollider().colliderect(c):
                
                if self.player.y<=c.y-self.player.image.get_rect().height+(20):
                    print("player y: %d" % self.player.y)
                    print("c.y: %d" % c.y)
                    self.player.vY=0
                    self.player.jumping=False
                    self.player.y=c.y-self.player.image.get_rect().height
                elif self.player.y>=c.y+c.height-20:
                    self.player.y=c.y+c.height
                    self.player.vY=0
                elif self.player.x<=c.x+20-self.player.getCollider().width:
                    self.player.x = c.x-self.player.getCollider().width
                elif self.player.x>=c.x-20+c.width:
                    self.player.x = c.x+c.width
    
    def drawScreen(self):
        self.surface.fill(BGCOLOR)
        for platform in self.platform:
            platform.draw(self.surface)
        self.player.draw(self.surface)
    
    def getCenterOfScreen(self):
        return (WINDOWWIDTH/2,WINDOWHEIGHT/2)
        
        
if __name__=='__main__':
    game = Game()
    game.main()
