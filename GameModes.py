from Pole import *
from Box import *

def Title(pg,width,height):
    textSize(20)
    pg.beginDraw()
    pg.background(102)
    pg.stroke(255)
    pg.strokeWeight(5)
    pg.line(mouseX/10, mouseY/10, 80 - mouseX/10, 60 - mouseY/10)
    pg.stroke(0)
    #pg.ellipse(mouseX/10,mouseY/10,1,1)
    #pg.ellipse(40,30,5,5)
    #dx = mouseX/10-40
    #dy = mouseY/10 - 30
    #if dy != 0:
        #pg.line(40,30,mouseX/10*tan(dx/dy),mouseY/10*tan(dx/dy))
        #print()
    pg.endDraw()
    for x in range(10):
        for y in range(10):
            image(pg, x*80,y*60) 
    if mouseX>100 and mouseX<300 and mouseY>500 and mouseY<560:
        stroke(255)
        fill(0)
        rect(100,500, 200, 60, 20)
        stroke(0)
        fill(255)
        text("PLAY THE GAME",122,535)
        
    else:
        stroke(0)
        fill(255)
        rect(100,500, 200, 60, 20)
        stroke(255)
        fill(0)
        text("PLAY THE GAME",122,535)
    
    
 
def Play(score):
     """
     Put Game here.
     """
     background(0)

def GameOver(score):
     # Game over screen. 
     textSize(32)
     fill(0)
     text(score, 10,40)
 
        
# Intersection test.  Returns true if balls are intersecting, false otherwise
def intersecting(b1,b2):
    if pow(b1.x-b2.x,2)+pow(b1.y-b2.y,2) <= pow(b1.R+b2.R,2):
        return True;
    return False
         