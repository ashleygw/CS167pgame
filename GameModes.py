from Pole import *
from Box import *

def Title(pg,width,height):
    textSize(20)
    
    #Makes the tile
    pg.beginDraw()
    pg.background(102)
    pg.stroke(255)
    pg.strokeWeight(5)
    pg.line(mouseX/10, mouseY/10, 80 - mouseX/10, 60 - mouseY/10)
    pg.stroke(0)
    pg.endDraw()
    
    #Draws the tile accross the screen
    for x in range(10):
        for y in range(10):
            image(pg, x*80,y*60) 
            
    #Play game button        
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
        
    #Exit game button    
    if mouseX>500 and mouseX<700 and mouseY>500 and mouseY<560:
        stroke(255)
        fill(0)
        rect(500,500, 200, 60, 20)
        stroke(0)
        fill(255)
        text("EXIT THE GAME",522,535)
    else:
        stroke(0)
        fill(255)
        rect(500,500, 200, 60, 20)
        stroke(255)
        fill(0)
        text("EXIT THE GAME",522,535)
    
    
def GameOver(score): #Make this pretty
     # Game over screen. 
     background(102)
     textSize(124)
     fill(0)
     text(score, 350,300)
     textSize(40)
     text("Good job you did it",230,400)
 
         