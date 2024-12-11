import pygame
import random as rn

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
dt = 0

nodi = []

labCol = 10
labRow = 10

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
    return startPos+(value*coefficente)


def drawLine(fromP, toP) :
    pygame.draw.line(screen, "#00a8f3", (applyCoefficente(fromP[0]), applyCoefficente(fromP[1])),
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

for l in range(10):
    # Controllo validità delle nuove coordinate
    newCoords = []
    while True:
        tcoords = rn.choice(coords)
        # Controllo uscita colonne
        if currCoords[0] == 0:
            if tcoords[0] == -1:
                continue
        if currCoords[0] == labCol-1:
            if tcoords[0] == 1:
                continue

        # Controllo uscita riga
        if currCoords[1] == 0:
            if tcoords[1] == -1:
                continue
        if currCoords[1] == labRow-1:
            if tcoords[1] == 1:
                continue

        newCoords = tcoords
        break

    oldCoords = currCoords
    currCoords[0] += newCoords[0]
    print(newCoords[0])
    currCoords[1] += newCoords[1]
    print(newCoords[1])
    print(str(oldCoords) + " " + str(currCoords))


print(nodi[9][3])

# drawLine((1, 3), (9, 4))

while True:
    pygame.display.update()
    clock.tick(60)
