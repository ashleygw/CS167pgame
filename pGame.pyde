from GameModes import *
from Vector import *
from Ball import *
from Player import *

def setup():
    global mode, pg, Balls, counter, score, Boxes, player, speedo, new_counter
    mode = 0
    pg = createGraphics(80,60) #P2D can be used here to make it run faster, it is less pretty though
    size(800,600) #P2D
    Balls = []
    counter = 0
    score = 0
    Boxes = []
    player = Player(Vector(80*5,60*5))
    speedo = 0 #Starting difficulty: 0 == easy, 80 == hardest, 100 == medium Needs work on pop expansion formula
    new_counter = 5
    
def draw():
    global mode, pg, Balls, counter,score, Boxes, player,speedo, new_counter
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
        background(102)
        textSize(32)
        fill(0)
        text(score, 10,40)
        player.render()
        player.update('x')
        for b in Boxes:
           b.render()
           if b.update():
               Boxes.remove(b)
               score+=1 
           if intersect(player, b):
               mode = 2
        counter +=1
        
        #Difficulty creep, currently not really needed as it gets harder with box behavior. Could implement in difficulty select.
        if score >=80:
            if random(0,1) > .96:
                fire()
        elif score >=50:
            if random(0,1) > .97:
                fire()
        elif score >= 30:
            if random(0,1) > .97:
                fire()
        elif score >= 20:
            if random(0,1)>.97:
                fire()
        else:
            if random(0,1)>.97:
                fire()
                
    if mode == 2:
        GameOver(score)
        
def drop():
    #Drops balls in title screen
    Balls.append(Ball(Vector(random(10,795),-10),Vector(random(-2,2),random(-2,2))))
    
def fire():
    #Generates boxes and throws them accross screen
    global speedo, score, Boxes
    speedo+=1
    var = floor(random(0,4))
    if score >= 35:
        if random(0,6) < 1:
            if score >= 50:
                print(50)
                for b in Boxes:
                    b.vel.setX(random(-3,3))
                    b.vel.setY(random(-3,3))
            else:
                for b in Boxes:
                    b.vel.setX(-b.vel.X())
                    b.vel.setY(-b.vel.Y())     
        if floor(var) == 0:
            Boxes.append(Box(Vector(-50,random(0,550)),Vector(random(2,6)),random(20,40)))
        if floor(var) == 1:
            Boxes.append(Box(Vector(850,random(0,550)),Vector(random(-6,-2)),random(20,40)))
        if floor(var) == 2:
            Boxes.append(Box(Vector(random(0,750),-50),Vector(0,random(2,6)),random(20,40)))        
        if floor(var) == 3:
            Boxes.append(Box(Vector(random(0,750),850),Vector(0,random(-6,-2)),random(20,40)))
    elif score>=20:
        if floor(var) == 0:
            Boxes.append(Box(Vector(-50,random(0,550)),Vector(random(2,6)),random(20,40)))
        if floor(var) == 1:
            Boxes.append(Box(Vector(850,random(0,550)),Vector(random(-6,-2)),random(20,40)))
        if floor(var) == 2:
            Boxes.append(Box(Vector(random(0,750),-50),Vector(0,random(2,6)),random(20,40)))        
        if floor(var) == 3:
            Boxes.append(Box(Vector(random(0,750),850),Vector(0,random(-6,-2)),random(20,40)))
    else:
        if floor(var) == 0:
            Boxes.append(Box(Vector(-50,random(0,550)),Vector(5,0),random(20,40)))
        if floor(var) == 1:
            Boxes.append(Box(Vector(850,random(0,550)),Vector(-5,0),random(20,40)))
        if floor(var) == 2:
            Boxes.append(Box(Vector(random(0,750),-50),Vector(0,5),random(20,40)))        
        if floor(var) == 3:
            Boxes.append(Box(Vector(random(0,750),850),Vector(0,-5),random(20,40)))
            
    
        
def mousePressed():
    #Used for button clicking
    global mode
    if mouseX>100 and mouseX<300 and mouseY>500 and mouseY<560:
        mode = 1        
    if mouseX>500 and mouseX<700 and mouseY>500 and mouseY<560:
        exit()
        
def intersect(player, b):
    #Checks if boxes intersect
    """
    if player.x > b.loc.X() + b.R or b.loc.X() > player.x + 80:
        return False
    if player.y < b.loc.Y() + b.R or b.loc.Y() < player.y + 60:
        return False
    """
    if player.x < b.loc.X() +b.R and player.x + 80 > b.loc.X() and player.y < b.loc.Y() + b.R and player.y + 60 > b.loc.Y():
        return True

def keyPressed():
    #Used for player controls
    global player
    if key == 'w':
        player.update('up')
    if key == 'a':
        player.update('left')
    if key == 's':
        player.update('down')
    if key == 'd':
        player.update('right')            
       