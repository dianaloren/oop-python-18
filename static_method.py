''' various tests in python '''

#Create a Class
class Ghost:
    
    #variable of the object
    lives = 10
    
    def __init__(self, name, color, speed, radius):
        assert type(speed) == int
        self.name = name
        self.color = color
        self.speed = speed
        self.radius = radius
        print("{} created".format(self.name))
     
      
    def __repr__(self):
        return '<{}, {}, {}>'.format(self.__class__.__name__, self.name, self.color, self.radius)
              
    def __str__(self):
        return '< {} , {}, {} >'.format(self.name, self.color, self.lives)
    
    def getName(self):
        return self.name
        
    def getSize(self):
        return self.circle_area(self.radius)
        
    @staticmethod
    def circle_area(r):      #size of ghost is basically its area considering the ghost a circle
        return r ** 2 * 3.14    # 3.14 is pi ... we can import math module
        
       
# Creating the object

g = Ghost("Bobby", "blue", 10, 4)
print("{} is size of {}".format(g.getName(), g.getSize()))
print("{} is size of {}".format(g.getName(), Ghost.circle_area(4)))
