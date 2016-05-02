from GameModes import *
from Vector import *
from Ball import *
def setup():
    global mode, pg, Balls
    mode = 0
    pg = createGraphics(80,60, P2D)
    size(800,600, P2D)
    Balls = []

    
def draw():
    global mode, pg, Balls
    if mode == 0:
        Title(pg,width,height)
        for b in Balls:
            b.render()
            if b.update(-.04, 1):
                Balls.remove(b)
    
            
def mousePressed():
    Balls.append(Ball(Vector(mouseX,mouseY),Vector(random(-2,2),random(-2,2))))

        
   