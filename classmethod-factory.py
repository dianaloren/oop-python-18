''' various tests in python '''

#Create a Class
class Ghost:
    
    #variable of the object
    lives = 10
    
    def __init__(self, name, color, speed):
        assert type(speed) == int
        self.name = name
        self.color = color
        self.speed = speed
        print("{} created".format(self.name))
     
      
    def __repr__(self):
        return '<{}, {}, {}>'.format(self.__class__.__name__, self.name, self.color)
              
    def __str__(self):
        return '< {} , {}, {} >'.format(self.name, self.color, self.lives)
    
    def getName(self):
        return self.name
        
    def reduceLife(self):
        self.lives -= 1
        print("You have now " + str(self.lives) + " lives.")   
        
    @classmethod
    def doSomethingWithLives(cls):
        cls.lives += 5
        print("Ghost earned 5 lives. Now it has " + str(cls.lives) + " lives.") 
    
    # Class method can be used as a factory function
    # The advantage of using "cls" is that we don't have to use the class name in the method. Useful if we decide to rename the class in the future. 
    @classmethod
    def YellowBobGhost(cls):
        return cls("Bob", "yellow", 10)
        
    @classmethod
    def RedAliceGhost(cls):
        return cls("Alice", "red", 10)
        
       
# Creating the object

bobghost = Ghost.YellowBobGhost()
aliceghost = Ghost.RedAliceGhost()
g = Ghost("n", "blue", 10)
print(type(bobghost))
print(type(g))
