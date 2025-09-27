from enum import Enum
import os
import pygame
import sys
from pygame import QUIT

class Symbol(Enum):
    NONE = 0
    X = 1
    O = 2
class Spot():
    def __init__(this, symbol):
        this.Symbol = symbol
    def updateSymbol(this, symbol):
        this.Symbol = symbol

def makeGameLines(x):
    pygame.draw.line(window, (0,0,0),(x,0),(x,800),100)
    pygame.draw.line(window, (0,0,0),(0,x), (800, x), 100)

def drawX(x,y):
    pygame.draw.line(window, (255,0,0),(x-100,y-100),(x+100,y+100),1)
    pygame.draw.line(window, (255,0,0),(x+100,y-100),(x-100,y+100),1)



pygame.init()
window = pygame.display.set_mode((800,800), 0 ,32)
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load(os.path.join("..","..","..","resources","ticTacToe.png")))
window.fill((255,255,255))

makeGameLines(250)
makeGameLines(550)
drawX(100,100)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()