from enum import Enum
import os
import pygame
import sys as System
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


pygame.init()
pygame.display.set_mode((1000,800), 0 ,32)
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load(os.path.join("..","..","..","resources","ticTacToe.png")))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            System.exit()