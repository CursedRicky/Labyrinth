import time

import pygame
import random as rn

import stack

# pygame setup
pygame.init()
pygame.display.set_caption("LabGen")
dt = 0

lines = []
nodi = []

# Settings
labCol = 25
labRow = 25
walls = True
visiblePaths = False
coefficente = 30
startPos = 50
autokill = rn.randint(40,50)
colorr = "#c71585"

screen = pygame.display.set_mode((labCol*35, labRow*35))
surface = pygame.Surface((labCol*35, labRow*35), pygame.SRCALPHA)
path = pygame.Surface((labCol*35, labRow*35), pygame.SRCALPHA)

screen.fill("#333333")
autokillCounter = 0

pygame.display.update()

class Nodo:
    pointTo = []
    visited = False
    start = False
    finish = False

    def __init__(self, column, row):
        self.row: int = row
        self.column: int = column

    def __str__(self):
        return str(self.column) + " " + str(self.row)


def applyCoefficente(value, starting=startPos) -> int:
    return starting + (value * coefficente)


if not visiblePaths:
    colorr+="00"

def drawLine(fromP, toP, color=colorr, w=5):
    lines.append(pygame.draw.line(path, color, (applyCoefficente(fromP[0]), applyCoefficente(fromP[1])),
                     (applyCoefficente(toP[0]), applyCoefficente(toP[1])), w))


for y in range(labRow):
    # y riga
    # i colonna
    for i in range(labCol):
        pygame.draw.circle(path, colorr, (applyCoefficente(i), applyCoefficente(y)), 5)

for r in range(labRow):
    rnodi = []
    for c in range(labCol):
        nodo = Nodo(c, r)
        rnodi.append(nodo)
    nodi.append(rnodi)

nodi[0][0].start = True
nodi[labCol-1][labRow-1].finish = False

#            C, R
currCoords = [0, 0]
oldCoords = [0, 0]
running = True
coords = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for l in range(labCol*labRow*2):
    autokillCounter += 1
    modify = False
    tC = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    tVisited = []
    # Controllo validità delle nuove coordinate
    newCoords = []
    currNodo = nodi[currCoords[0]][currCoords[1]]
    # Controllo uscita colonne
    if currCoords[0] == 0:
        tC.remove([-1, 0])
    if currCoords[0] == labCol - 1:
        tC.remove([1, 0])

    # Controllo uscita riga
    if currCoords[1] == 0:
        tC.remove([0, -1])
    if currCoords[1] == labRow - 1:
        tC.remove([0, 1])

    ta = []
    rn.shuffle(tC)
    for tt in tC:
        if not nodi[currCoords[0]+tt[0]][currCoords[1]+tt[1]].visited:
            ta.append(tt)

    try:
        tcoords = rn.choice(ta)
    except:
        modify = True

    if autokillCounter == autokill:
        autokillCounter = 0
        modify = True
        autokill = rn.randint(10, 15)

    newCoords = tcoords

    currNodo.visited = True
    if not modify:
        drawLine(currCoords, (currCoords[0] + newCoords[0], currCoords[1] + newCoords[1]))
        nodi[currCoords[0]][currCoords[1]].pointTo = [currCoords[0] + newCoords[0], currCoords[1] + newCoords[1]]
        pygame.display.update()
        currCoords[0] += newCoords[0]
        currCoords[1] += newCoords[1]
    else:
        ctrl = True
        riga = 0
        colonna = 0
        for r in nodi:
            for c in r:
                if c.visited and ctrl:
                    tC = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                    if c.column == 0:
                        tC.remove([-1, 0])
                    if c.column == labCol - 1:
                        tC.remove([1, 0])

                    if c.row == 0:
                        tC.remove([0, -1])
                    if c.row == labRow - 1:
                        tC.remove([0, 1])

                    ta = []
                    rn.shuffle(tC)
                    for tt in tC:
                        if not nodi[c.column + tt[0]][c.row + tt[1]].visited:
                            ta.append(tt)
                    if len(ta) == 0:
                        continue
                    else:
                        currCoords[0] = c.column
                        currCoords[1] = c.row
                        ctrl = False
                        break


if walls:
    pygame.draw.line(screen, "white", (applyCoefficente(0, 35), applyCoefficente(labCol, 35)),
                     (applyCoefficente(labCol - 1, 65), applyCoefficente(labCol, 35)), 2)

    pygame.draw.line(screen, "white", (applyCoefficente(labCol, 35), applyCoefficente(0, 35)),
                     (applyCoefficente(labCol - 1, 65), applyCoefficente(labCol-1, 35)), 2)

    for r in nodi:
        for c in r:
            if not pygame.draw.line(surface, (0,0,0,0), (applyCoefficente(c.column, 35), applyCoefficente(c.row, 35)),
                                    (applyCoefficente(c.column, 65), applyCoefficente(c.row, 35)), 1).collideobjects(
                lines):
                pygame.draw.line(screen, "white", (applyCoefficente(c.column, 35), applyCoefficente(c.row, 35)),
                                 (applyCoefficente(c.column, 65), applyCoefficente(c.row, 35)), 2)

    for r in nodi:
        for c in r:
            if not pygame.draw.line(surface, (0,0,0,0), (applyCoefficente(c.column, 35), applyCoefficente(c.row, 35)),
                                    (applyCoefficente(c.column - 1, 65), applyCoefficente(c.row + 1, 35)),
                                    1).collideobjects(lines):
                if not c.start:
                    pygame.draw.line(screen, "white", (applyCoefficente(c.column, 35), applyCoefficente(c.row, 35)),
                                     (applyCoefficente(c.column - 1, 65), applyCoefficente(c.row + 1, 35)), 2)

screen.blit(surface, (0,0))
screen.blit(path, (0,0))
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
