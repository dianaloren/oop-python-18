import math

class Ghost:

    lives = 10
    
    def __init__(self, name, color, speed, radius):
        self.name = name
        self.color = color
        self.speed = speed
        self.radius = radius
        print("{} was created".format(self.name))
        
    def __repr__(self):
        return "{}, {}, {}, {}".format(self.__class__.___name__, self.name, self.color, self.speed)
        
    def __str__(self):
        return  "{}, {}, {}".format(self.name, self.color, self.speed)
        
    def getSize(self):
        return self.circle_area(self.radius)
        
    @classmethod
    def doSomething(cls):
        cls.lives += 5
        print("Ghost CLASS has now 5 more lives. Now it has {} lives".format(str(cls.lives)))
        
    #Factory
    @classmethod
    def YellowBobGhost(cls):
        return cls("BobYell", "yellow", 10, 5)
        
    def RedBobGhost(cls):
        return cls("BobRed", "red", 10, 5)
        
    # Static Method
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
        
        
g = Ghost("Bob", "red", 10, 4)
print("Bob lives", g.lives)
print("Ghost lives ", Ghost.lives)

# change lives of Bob
g.lives = 1
print("Bob lives", g.lives)

g1 = Ghost("Bobby", "blue", 10, 5)
print("Bobby lives", g1.lives)

g2 = Ghost.YellowBobGhost()
print(g2.name)

print(g.circle_area(3))
print(g.getSize())

g.doSomething()
print("{} has {} lives".format(g.name, g.lives))
print("{} has {} lives".format(g1.name, g1.lives))
g.doSomething()
print("{} has {} lives".format(g.name, g.lives))
print("{} has {} lives".format(g1.name, g1.lives))

Ghost.lives = 25
print("{} has {} lives".format(g.name, g.lives))
print("{} has {} lives".format(g1.name, g1.lives))

print(dir(g1))










