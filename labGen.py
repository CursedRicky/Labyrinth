import time

import pygame
import random as rn

import stack

# pygame setup
pygame.init()
clock = pygame.time.Clock()
dt = 0

nodi = []

labCol = 10
labRow = 10

screen = pygame.display.set_mode((labCol*35, labRow*35))

coefficente = 30
startPos = 50

screen.fill("#333333")


class Nodo:
    pointTo = []
    visited = False

    def __init__(self, column, row):
        self.row: int = row
        self.column: int = column

    def __str__(self):
        return str(self.column) + " " + str(self.row)


def applyCoefficente(value) -> int:
    return startPos + (value * coefficente)


def drawLine(fromP, toP, color="#00a8f3"):
    pygame.draw.line(screen, color, (applyCoefficente(fromP[0]), applyCoefficente(fromP[1])),
                     (applyCoefficente(toP[0]), applyCoefficente(toP[1])), 5)


for y in range(labRow):
    # y riga
    # i colonna
    for i in range(labCol):
        pygame.draw.circle(screen, "#00a8f3", (applyCoefficente(i), applyCoefficente(y)), 5)

for r in range(labRow):
    rnodi = []
    for c in range(labCol):
        nodo = Nodo(c, r)
        rnodi.append(nodo)
    nodi.append(rnodi)

#            C, R
currCoords = [0, 0]
oldCoords = [0, 0]
running = True
coords = [[0, 1], [1, 0], [0, -1], [-1, 0]]

autokill = rn.randint(10,15)
autokillCounter = 0

for l in range(labCol*labRow):
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
        pygame.display.update()
        time.sleep(.5)
        currCoords[0] += newCoords[0]
        currCoords[1] += newCoords[1]
    else:
        ctrl = True
        riga = 0
        colonna = 0
        while ctrl:
            tC = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            if nodi[colonna][riga].visited:
                node = nodi[colonna][riga]
                if node.column == 0:
                    tC.remove([-1, 0])
                if node.column == labCol - 1:
                    tC.remove([1, 0])

                # Controllo uscita riga
                if node.row == 0:
                    tC.remove([0, -1])
                if node.row == labRow - 1:
                    tC.remove([0, 1])

                ta = []
                rn.shuffle(tC)
                for tt in tC:
                    if not nodi[colonna + tt[0]][riga + tt[1]].visited:
                        ta.append(tt)




                print(len(ta))
                if len(ta) > 0:
                    currCoords[0] = colonna
                    currCoords[1] = riga
                    ctrl = False

                else :
                    colonna += 1
                    if colonna == labCol:
                        colonna = 0
                        riga += 1
                '''
            else :
                colonna+=1
                if colonna == labCol:
                    colonna = 0
                    riga+=1
                if riga == 10:
                    ctrl = False
                print("B")
            '''


print("finito")

    # print(currCoords)

# drawLine((1, 3), (9, 4))

while True:
    pygame.display.update()
    clock.tick(60)
