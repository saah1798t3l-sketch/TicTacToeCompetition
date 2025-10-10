from enum import Enum
import os
import pygame
import sys

class Symbol(Enum):
    NONE = 0
    X = 1
    O = 2
class Spot:
    def __init__(self, buttonX, buttonY):
        self.symbol = Symbol.NONE
        self.rectangle = pygame.Rect(buttonX, buttonY, 225, 225)
    def updateSymbol(self, symbol):
        self.symbol = symbol
    def __eq__(self, otherSpot):
        return self.symbol == otherSpot.symbol

def makeGameLines(LineXCoordinate):
    pygame.draw.line(window, (0,0,0), (LineXCoordinate, 0), (LineXCoordinate, 775), 50)
    pygame.draw.line(window, (0,0,0), (0, LineXCoordinate), (775, LineXCoordinate), 50)

def drawX(xCoordinate, yCoordinate):
    pygame.draw.line(window, (255,0,0), (xCoordinate - 75, yCoordinate - 100), (xCoordinate + 100, yCoordinate + 100), 50)
    pygame.draw.line(window, (255,0,0), (xCoordinate + 100, yCoordinate - 100), (xCoordinate - 75, yCoordinate + 100), 50)
def drawO(xCordinate,yCordinate):
    pygame.draw.circle(window, (0,100,255),(xCordinate,yCordinate), 100,50)

def checkWin():
    for i in range(0,9,3):
        if (s:= spots[i]) == spots[i + 1] and spots[i] == spots[i + 2] and s.symbol != Symbol.NONE:
            pygame.draw.line(window, (128,50,127), (s.rectangle.x+112.5, s.rectangle.y), (spots[i+2].rectangle.x+112.5, spots[i+2].rectangle.y+225), 50)
            return s.symbol

    for i in range(0,3):
        if (s:= spots[i]) == spots[i + 3] and spots[i] == spots[i + 6] and s.symbol != Symbol.NONE:
            pygame.draw.line(window, (128,50,127), (s.rectangle.x-112.5, s.rectangle.y+112.5), (spots[i+6].rectangle.x+255, spots[i+6].rectangle.y+112.5), 50)
            return s.symbol
    if ((leftToRight := (spots[0] == spots[4] and spots[0] == spots[8])) or (spots[2] == spots[4] and spots[2] == spots[6])) and spots[4].symbol != Symbol.NONE:
        x = (0,0) if leftToRight else (775,0)
        y = (775,775) if leftToRight else (0,775)
        pygame.draw.line(window, (128,50,127), x, y, 50)
        return spots[4].symbol
    return Symbol.NONE
def checkTie():
    for place in spots:
        if place.symbol == Symbol.NONE:
            return False
    return True

turn = Symbol.X




pygame.init()
window = pygame.display.set_mode((775,850), 0 ,32)
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load(os.path.join("..","..","..","resources","ticTacToe.png")))
window.fill((255,255,255))


makeGameLines(250)
makeGameLines(525)
spots = [] #Triplets = Columns
for x in (n := range(0, 825,275)):
    for y in n:
        spots.append(Spot(x, y))

pygame.display.update()
font = pygame.font.SysFont("Times New Roman", 30)
while True:
    if turn != Symbol.NONE:
        textImage = font.render(f"{turn.name} to move", True, (0, 0, 0), (255, 255, 255))
        window.blit(textImage, (325,810))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and turn != Symbol.NONE:
            position = event.pos
            for spot in spots:
                if spot.rectangle.collidepoint(position) and spot.symbol == Symbol.NONE:
                    if turn == Symbol.X:
                        drawX(spot.rectangle.x +100, spot.rectangle.y+112.5)
                        spot.symbol = Symbol.X
                    else:
                        drawO(spot.rectangle.x +112.5, spot.rectangle.y+112.5)
                        spot.symbol = Symbol.O
                    turn = Symbol.O if turn == Symbol.X else Symbol.X
            if (w := checkWin()) != Symbol.NONE:
                textImage = font.render(f"{w.name} has won the game!", True, (0,0,0), (255,255,255))
                window.blit(textImage, (275,810))
                turn = Symbol.NONE
            elif checkTie():
                textImage = font.render("The game was tied!", True, (0,0,0), (255,255,255))
                window.blit(textImage, (275,810))
                turn = Symbol.NONE

    pygame.display.update()