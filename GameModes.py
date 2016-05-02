from Pole import *
from Box import *
def Title(pg,width,height):
    
    pg.beginDraw()
    pg.background(102)
    pg.stroke(255)
    pg.strokeWeight(5)
    pg.line(mouseX/10, mouseY/10, 40, 30)
    pg.stroke(0)
    pg.ellipse(mouseX/10,mouseY/10,5,5)
    pg.ellipse(40,30,5,5)
    #dx = mouseX/10-40
    #dy = mouseY/10 - 30
    #if dy != 0:
        #pg.line(40,30,mouseX/10*tan(dx/dy),mouseY/10*tan(dx/dy))
        #print()
    pg.endDraw()
    for x in range(10):
        for y in range(10):
            image(pg, x*80,y*60) 
    #stroke(0)
    #fill(255)
    #rect(100,500, 200, 60, 20)
    
 
def PlayMode(score):
     for i in range(len(Balls)):
         for j in range(i+1,len(Balls)):
             if intersecting(Balls[i],Balls[j]):
                 Balls[i].setIntersecting(True)
                 Balls[j].setIntersecting(True)
             
     
     # Current score
     textSize(32)
     fill(0)
     text(score, 10,40)
     # If currtime exceeds endtime, turn off playmode
     playmode = True
     return playmode

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
         