import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
dt = 0

labL = 10
labH = 10

coefficente = 30
startPos = 50

def applyCoefficente(value) -> int:
    return startPos+(value*coefficente)

def drawLine(fromP, toP) :
    pygame.draw.line(screen, "#00a8f3", (applyCoefficente(fromP[0]), applyCoefficente(fromP[1])),
                     (applyCoefficente(toP[0]), applyCoefficente(toP[1])), 5)

screen.fill("#333333")

for y in range(labH):
    # y riga
    # i colonna
    for i in range(labL):
        pygame.draw.circle(screen, "#00a8f3", (applyCoefficente(i), applyCoefficente(y)), 5)

drawLine((1, 2), (1, 3))

while True:
    pygame.display.update()
    clock.tick(60)
