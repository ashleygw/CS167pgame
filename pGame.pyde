from GameModes import *
from Vector import *
from Ball import *
def setup():
    global mode, pg, Balls, counter
    mode = 0
    pg = createGraphics(80,60, P2D)
    size(800,600, P2D)
    Balls = []
    counter = 0
    
def draw():
    global mode, pg, Balls, counter
    counter += 1
    if mode == 0:
        Title(pg,width,height)
        for b in Balls:
            b.render()
            if b.update(-.04, 1):
                Balls.remove(b)
        if counter % 60 == 0:
            drop()
    
            
def drop():
    Balls.append(Ball(Vector(random(10,795),-10),Vector(random(-2,2),random(-2,2))))

        
   