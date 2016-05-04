
class Player:
    def __init__(self,pos):
        self.x = pos.X()
        self.y = pos.Y()
        #self.vy = vy
        #self.ay = ay
        self.c = color(random(255),random(255),random(255))
        #self.t=0
        #self.dt=0.1
        #self.bottom = bottom
         
    def render(self):
        noStroke()
        fill(self.c)
        #rect(width/2-100,height/2+self.y,width/2-50,height/2+self.bottom)
        rect(self.x,self.y,80,60)
        fill(color(random(255),random(255),random(255)))
        ellipse(self.x + 20, self.y +20,20,10)
        ellipse(self.x + 58, self.y +20,20,10)
        
    def update(self, dir):
        #Fix this
        if dir == "up" and self.y >= 60:
            self.y -= 60
        if dir == "down" and self.y < 540:
            self.y += 60
        if dir == "left" and self.x >= 80:
            self.x -= 80
        if dir == "right" and self.x < 720:
            self.x += 80
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    #def jump(self):
     #   """jumps by raising bottom corner coordinate of rectangle"""
        #update time
      #  self.t += self.dt
        #raise corner
       # if self.bottom > 200:
        #    self.bottom = self.bottom - 25*sin(10*self.t)
        #else:
         #   self.bottom = self.bottom + 25*sin(10*self.t)
       
        #alternative:
        #run a function raising corner until
        #top corner equals a particular value.
        #Then, run a function lowering the corner.  
                              
    #def crouch(self):
        """crouches by lowering top left corner"""
        #update time
        #self.t += self.dt
        #lower top corner sinusodially
        #if self.y < height/2+25:
         #   self.y = self.y + 25*sin(10*self.t)
        #else:
         #   self.y = self.y - 25*sin(10*self.t)
                    
        #alternative:
        #run a function lowering corner until
        #top corner equals a particular value.
        #Then, run a function raising the corner. 