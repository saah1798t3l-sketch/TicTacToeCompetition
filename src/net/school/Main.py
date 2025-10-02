from enum import Enum
import os
import pygame
import sys

class Symbol(Enum):
    NONE = 0
    X = 1
    O = 2
class Spot:
    def __init__(this, symbol, buttonX, buttonY):
        this.symbol = symbol
        this.rectangle = pygame.Rect(buttonX, buttonY, 200, 200)
    def updateSymbol(this, symbol):
        this.symbol = symbol

def makeGameLines(x):
    pygame.draw.line(window, (0,0,0),(x,0),(x,800),50)
    pygame.draw.line(window, (0,0,0),(0,x), (800, x), 50)

def drawX(x,y):
    pygame.draw.line(window, (255,0,0),(x-100,y-100),(x+100,y+100),50)
    pygame.draw.line(window, (255,0,0),(x+100,y-100),(x-100,y+100),50)
def drawO(x,y):
    pygame.draw.circle(window, (0,100,255),(x,y), 100,50)

def checkWin():
   pass

XTurn = True




pygame.init()
window = pygame.display.set_mode((800,850), 0 ,32)
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load(os.path.join("..","..","..","resources","ticTacToe.png")))
window.fill((255,255,255))


makeGameLines(250)
makeGameLines(549)
spots = [] #Inner arrays = Columns!!! (vertical!!!)
for x in (n := range(0, 900,300)):
    for y in n:
        spots.append(Spot(Symbol.NONE, x, y))

buttonA = pygame.Rect(0,0,200,200)
buttonB = pygame.Rect(0,300,200,200)


pygame.display.update()
while True:
    font = pygame.font.SysFont("Times New Roman", 30)
    textImage = font.render(("X" if XTurn else "O") +" to move", True, (0,0,0), (255,255,255))
    window.blit(textImage, (350,810))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            for spot in spots:
                if spot.rectangle.collidepoint(position) and spot.symbol == Symbol.NONE:
                    if XTurn:
                        drawX(spot.rectangle.x +100, spot.rectangle.y+100)
                        spot.symbol = Symbol.X
                    else:
                        drawO(spot.rectangle.x +100, spot.rectangle.y+100)
                        spot.symbol = Symbol.O
                    XTurn = not XTurn
    pygame.display.update()