from GameModes import *
from Vector import *
from Ball import *
from Player import *
def setup():
    global mode, pg, Balls, counter, score, Boxes, player, speedo
    mode = 0
    pg = createGraphics(80,60) #P2D
    size(800,600) #P2D
    Balls = []
    counter = 0
    score = 0
    Boxes = []
    player = Player(Vector(80*5,60*5))
    speedo = 0
    
def draw():
    global mode, pg, Balls, counter,score, Boxes, player,speedo
    
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
        #print(round(random(0,4)))
        Play(score)    
        player.render()
        player.update('x')
        for b in Boxes:
           b.render()
           if b.update():
               Boxes.remove(b)
               score+=1 
           if intersect(player, b):
               return "Lose"
        counter +=1
        if counter%(100-speedo) == 0:
            print(Boxes)
            fire()
    if mode == 2:
        print("LOSE")
        
                
    
            
def drop():
    Balls.append(Ball(Vector(random(10,795),-10),Vector(random(-2,2),random(-2,2))))
    
def fire():
    global speedo
    print(speedo)

    speedo+=1
        
    if round(random(0,3)) == 0.0:
        Boxes.append(Box(Vector(-50,random(0,550)),Vector(5,0),0))
    if round(random(0,3)) == 1.0:
        Boxes.append(Box(Vector(850,random(0,550)),Vector(-5,0),0))
    if round(random(0,3)) == 2.0:
        Boxes.append(Box(Vector(random(0,750),-50),Vector(0,5),0))        
    if round(random(0,3)) == 3.0:
        Boxes.append(Box(Vector(random(0,750),850),Vector(0,-5),0))
        
def mousePressed():
    global mode
    if mouseX>100 and mouseX<300 and mouseY>500 and mouseY<560:
        mode = 1        
        
def intersect(player, b):
    return False


def keyPressed():
    global player
    if key == 'w':
        player.update('up')
    if key == 'a':
        player.update('left')
    if key == 's':
        player.update('down')
    if key == 'd':
        player.update('right')            
       