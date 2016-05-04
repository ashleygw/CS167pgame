class Vector:
    """ A class to represent 2D Vectors, i.e. <1,2>. """
    def __init__(self,x=0,y=0):
        """ Create a new Vector object. """
        self.x = x
        self.y = y
        pass

    def __str__(self):
        """ Convert to string for printing purposes. """
        return "<" + str(self.x) + "," +  str(self.y) + ">"
        pass

    def __eq__(self,other):
        """ Test equality of Vector objects using ==. """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        pass

    def __ne__(self,other):
        """ Test inequality of Vector objects using !=. """
        if self.x != other.x or self.y != other.y:
            return True
        else:
            return False
        pass

    def __add__(self,other):
        """ Add two Vector objects using the + operator. """
        return Vector(self.x + other.x, self.y+other.y)
        pass
        
    def __sub__(self,other):
        """ - two Vector objects using the - operator. """
        return Vector(self.x - other.x, self.y-other.y)
        pass

    def __mul__(self,a):
        """ Perform scalar multiplication using the * operator. """
        return Vector(self.x*a,self.y*a)
        pass

    def __rmul__(self,a):
        """ Perform scalar multiplication using the * operator.
        Allows the scalar to appear on the left of the Vector."""
        return Vector(self.x*a,self.y*a)
        pass

    def __iadd__(self,other):
        """ Perform Vector increments using the += operator. """
        return Vector(self.x + other.x, self.y + other.y)
        pass

    def setX(self, x):
        """ Set the x coordinate. """
        self.x = x
        pass

    def setY(self, y):
        """ Set the y coordinate. """
        self.y = y
        pass

    def X(self):
        """ Return the x coordinate. """
        return self.x
        pass

    def Y(self):
        """ Return the y coordinate. """
        return self.y
        pass
    def dotp(self,rhs):
        return self.x * rhs.x + self.y * rhs.y
    
    def le(self):
        return sqrt(self.x*self.x + self.y*self.y)
