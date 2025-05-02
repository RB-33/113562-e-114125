from graphics import *
from time import sleep
import math as m

def main():
    win = GraphWin("Bola saltitante", 400, 400)
    win.setCoords(-100, -100, 100, 100)

    shape = Circle(Point(0,-80),10)
    shape.setOutline("black")
    shape.setFill("yellow")
    shape.draw(win)

    dx = 1
    dy = 1

    for i in range(10000):
        c = shape.getCenter()
        
        if c.getX() > 90:
            dx = -1
        elif c.getX() < -90:
            dx = 1
        elif c.getY() > 90:
            dy = -1
        elif c.getY() < -90:
            dy = 1

        sleep(0.005)
        shape.move(dx,dy)
        if win.checkMouse() is not None:
            break
            
    win.close()

main()