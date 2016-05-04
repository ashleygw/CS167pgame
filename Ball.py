from Vector import *
#This only works for the title screen, don't try to use this in the main game. Balls will not behave.
class Ball:
    def __init__(self, pos, vel, radius=10):
        self.x = pos.X()
        self.y = pos.Y()
        self.c = color(random(255),random(255),random(255),255)
        self.R = radius
        self.vx = vel.X()
        self.vy = vel.Y()
        self.pmx = mouseX/10
        self.pmy = mouseY/10
        
    def render(self):
        """ Draw the ball for time t. """
        noStroke()
        fill(self.c)
        ellipse(self.x,self.y,self.R,self.R)
    
    def update(self, acceleration, E):
        """ Responsible for time keeping. """
        # Update the velocity for gravity
        self.vy -= acceleration
        
        #Basic Wall interaction
        if self.x >= width - 10:
            self.x = width - 11
            self.vx = -self.vx*E
        if self.y >= height:
            return True
        if self.x <= 5:
            self.x = 6
            self.vx = abs(self.vx*E)
        if self.y <= 5:
            self.y = 6
            self.vy =  abs(self.vy*E)
            
        #Line interaction
        p0 = Vector(mouseX/10, mouseY/10)
        p1 = Vector(80 - mouseX/10, 60 - mouseY/10)
        be = Vector(self.x%80 + self.vx, self.y%60+ self.vy)
        bs = Vector(self.x%80, self.y%60)
        xblo = floor(self.x/80)
        yblo = floor(self.y/60)   
        temp = p0 - p1
        n = Vector(-temp.Y(),temp.X())   
        
        #No collision case
        if n.le() == 0:
            self.x += self.vx
            self.y += self.vy
            return
        
        n = n*(1/n.le())
        v = Vector(self.vx,self.vy) 
        d = self.R
        
        #if n.dotp(bs) - n.dotp(p0) < 0: #This is test code for preventing the ball from going through moving lines
            #d = -d
            
        t = (n.dotp(p0) - n.dotp(bs)) / n.dotp(v) #+d?
        #t2 = (n.dotp(p0) - n.dotp(bs)) / n.dotp(v) #+d?
        bi = bs + v*t
        #bi2 = bs + v*t2    
        
        q = bi - p0
        r = bi - p1
        d0 = (p0 - bi).le()
        d1 = (p1 - bi).le()
        
        #Another collision check
        if q.dotp(r)> 0 or (t<0 or t>1):
            self.x += self.vx
            self.y += self.vy
            return
        
        """ #Further line movement collision testing
        if (t<0 or t>1):
            if not (d0<self.R or d1<self.R):
                self.x += self.vx
                self.y += self.vy
                print("b")
                return
            else:
                print("a")
        """
        
        i = be - bi
        s = i.dotp(n) * n
        u = i-2*s
        bep = u + bi
        nv = u* (1 / u.le())
        speed = v.le()
        self.vx = nv.X()*speed*.95 #This slows it down a little
        self.vy = nv.Y()*speed*.95 #This slows it down a little
        self.x = bep.X() + xblo*80
        self.y = bep.Y() + yblo*60
        
        
        
        
        
        #VVVVVVVVV Old collision CODE DON"T UNCOMMENT ANY OF THIS VVVVVVV
        # Checks for Line interaction   
        #TF LOCAL COORDS
        #NEED FOR LOOP CHECKING FOR MORE THAN JUST ONE INTERACTION
        """
        if not self.x%80 > 40 and mouseX < 400:
            
            LP1x, LP1y = mouseX/10 - self.x%80, mouseY/10 - self.y%60
            LP2x, LP2y = 40 - self.x%80, 30 - self.y%60
            #PRECALC
            p2mp1x, p2mp1y = LP2x - LP1x, LP2y - LP1y 
            #stroke(5)
            #line(LP1x,LP1y,LP2x,LP2y)
            a = (p2mp1x) * (p2mp1x) + (p2mp1y) * (p2mp1y)
            b = 2 * ((p2mp1x * LP1x) + (p2mp1y * LP1y))
            c = (LP1x * LP1x) + (LP1y * LP1y) - (10 * 10)
            delta = b * b - (4 * a * c)
            #if (delta < 0) #No intersection
                #pass
            
            #if (delta == 0):
                #u = -b / (2 * a)
                #print(LP1x)
                #print(LP1y)
                #print(str(LP1x + u * p2mp1x),str( LP1y + u * p2mp1y))
                #point of collision: x , y 
            if (delta > 0):
                SquareRootDelta = sqrt(delta)
                u1 = (-b + SquareRootDelta) / (2 * a)
                u2 = (-b - SquareRootDelta) / (2 * a)
                #print(str(mouseX/800.0*80 + u1 * p2mp1x), str(mouseY/600.0 * 60 + u1*p2mp1y), str(mouseX/800.0*80 + u2 * p2mp1x),str( mouseY/600.0 * 60 + u2*p2mp1y))
                #ellipse(mouseX/800.0*80 + u1 * p2mp1x,mouseY/600.0 * 60 + u1*p2mp1y, 20,20)
                #ellipse(mouseX/800.0*80 + u2 * p2mp1x,mouseY/600.0 * 60 + u2*p2mp1y, 20,20)
                #stroke(3)
                #line(mouseX/800.0*80 + u1 * p2mp1x, mouseY/600.0 * 60 + u1*p2mp1y, mouseX/800.0*80 + u2 * p2mp1x , mouseY/600.0 * 60 + u2*p2mp1y)
                
            
                angle = degrees(atan2(self.vy, self.vx))
                if 30.0- mouseY/600.0 * 60.0 == 0:
                    normalAngle = 0
                else:
                    normalAngle = degrees(atan((40.0-mouseX/800.0*80.0)/(30.0- mouseY/600.0 * 60.0)))
                angle = 2 * normalAngle - 180 - angle
                mag = sqrt(self.vx*self.vx + self.vy*self.vy)
                
                self.vx = -cos(radians(angle)) * mag;
                self.vy = sin(radians(angle)) * mag;
                #self.x += self.vx
                #self.y += self.vy
            
        if not self.x%80 < 40 and mouseX > 400:
            LP1x, LP1y = mouseX/10 - self.x%80, mouseY/10 - self.y%60
            LP2x, LP2y = 40 - self.x%80, 30 - self.y%60
            #PRECALC
            p2mp1x, p2mp1y = LP2x - LP1x, LP2y - LP1y 
            #stroke(5)
            #line(LP1x,LP1y,LP2x,LP2y)
            a = (p2mp1x) * (p2mp1x) + (p2mp1y) * (p2mp1y)
            b = 2 * ((p2mp1x * LP1x) + (p2mp1y * LP1y))
            c = (LP1x * LP1x) + (LP1y * LP1y) - (10 * 10)
            delta = b * b - (4 * a * c)
            #if (delta < 0) #No intersection
                #pass
            
            #if (delta == 0):
                #u = -b / (2 * a)
                #print(LP1x)
                #print(LP1y)
                #print(str(LP1x + u * p2mp1x),str( LP1y + u * p2mp1y))
                #point of collision: x , y 
            if (delta > 0):
                SquareRootDelta = sqrt(delta)
                u1 = (-b + SquareRootDelta) / (2 * a)
                u2 = (-b - SquareRootDelta) / (2 * a)
                #print(str(mouseX/800.0*80 + u1 * p2mp1x), str(mouseY/600.0 * 60 + u1*p2mp1y), str(mouseX/800.0*80 + u2 * p2mp1x),str( mouseY/600.0 * 60 + u2*p2mp1y))
                #ellipse(mouseX/800.0*80 + u1 * p2mp1x,mouseY/600.0 * 60 + u1*p2mp1y, 20,20)
                #ellipse(mouseX/800.0*80 + u2 * p2mp1x,mouseY/600.0 * 60 + u2*p2mp1y, 20,20)
                #stroke(3)
                #line(mouseX/800.0*80 + u1 * p2mp1x, mouseY/600.0 * 60 + u1*p2mp1y, mouseX/800.0*80 + u2 * p2mp1x , mouseY/600.0 * 60 + u2*p2mp1y)
                
            
                angle = degrees(atan2(self.vy, self.vx))
                if 30.0- mouseY/600.0 * 60.0 == 0:
                    normalAngle = 0
                else:
                    normalAngle = degrees(atan((40.0-mouseX/800.0*80.0)/(30.0- mouseY/600.0 * 60.0)))
                angle = 2 * normalAngle - 180 - angle
                mag = sqrt(self.vx*self.vx + self.vy*self.vy)
                
                self.vx = -cos(radians(angle)) * mag;
                self.vy = sin(radians(angle)) * mag;
                #self.x += self.vx
                #self.y += self.vy
            """
        
    