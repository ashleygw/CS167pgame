from GameModes import *
from Vector import *
from Ball import *
def setup():
    global mode, pg, Balls, counter, score, Boxes
    mode = 0
    pg = createGraphics(80,60) #P2D
    size(800,600) #P2D
    Balls = []
    counter = 0
    score = 0
    Boxes = []
    
def draw():
    global mode, pg, Balls, counter,score, Boxes
    
    if mode == 0:
        counter += 1
        Title(pg,width,height)
        for b in Balls:
            b.render()
            if b.update(-.04, 1):
                Balls.remove(b)
        if counter % 60 == 0:
            drop()
    if mode == 1:
        Play(score)    
        for b in Boxes:
           b.render()
           if b.update():
               Boxes.remove(b) 
           if b.update() == "Lose":
               mode = 2
        counter +=1
        if counter%60 == 0:
            print(Boxes)
            fire()
            score += 1
    if mode == 2:
        print("LOSE")
        
                
    
            
def drop():
    Balls.append(Ball(Vector(random(10,795),-10),Vector(random(-2,2),random(-2,2))))
    
def fire():
    Boxes.append(Box(Vector(850,500),Vector(-5,0),0))

def mousePressed():
    global mode
    if mouseX>100 and mouseX<300 and mouseY>500 and mouseY<560:
        mode = 1        
   