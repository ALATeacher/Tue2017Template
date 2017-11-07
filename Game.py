'''
@author: ALATeacher
Description: 
'''
import pygame
import sys, os, math
from pygame import *
from random import randint

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GAMENAME = "Awesome Game"
FRAMERATE = 60
BGCOLOR = (255,255,255)

class Game:
    ##########VARIABLES##########
    score = 0
    levels = []
    
    
    ##########CONSTRUCTOR##########
    def __init__(self):
        pass
    
    #########MAIN FUNCTION##########
    def main(self):
        playing = True
        pygame.init()
        clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption(GAMENAME)
        
        ##########GAME LOOP##########
        while playing:
            pass
        
        
        
if __name__=='__main__':
    game = Game()
    game.main()
        
    


