class Box:
    def __init__(self,loc, vel, Size):
        self.loc = loc
        self.vel = vel
        self.type = type
        self.R = Size
        self.c = color(random(255),random(255),random(255),255)
        pass
        
    def update(self):
        #Update box position, delete box if out of range.
        self.loc += self.vel
        if self.loc.X() < -100 or self.loc.X() > 950:
            return True
        if self.loc.Y() < -100 or self.loc.Y() > 900:
            return True
        
    def render(self):
        #Draw the box
        noStroke()
        fill(self.c)
        rect(self.loc.X(),self.loc.Y(),self.R,self.R)
