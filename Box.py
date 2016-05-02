class Box:
    def __init__(self,loc, vel, type):
        self.loc = loc
        self.vel = vel
        self.type = type
        self.R = 20
        self.c = color(random(255),random(255),random(255),255)
        pass
    def update(self):
        self.loc += self.vel
        if self.loc.X() < -100 or self.loc.X() > 900:
            return True
        
        #if intersectswithplayer:
            #return "Lose"
        
    def render(self):
        """ Draw the ball for time t. """
        noStroke()
        fill(self.c)
        rect(self.loc.X(),self.loc.Y(),self.R,self.R)
        
    # Intersection test.  Returns true if balls are intersecting, false otherwise
    def intersecting(b1,b2):
        if pow(b1.x-b2.x,2)+pow(b1.y-b2.y,2) <= pow(b1.R+b2.R,2):
            return True;
        return False
         