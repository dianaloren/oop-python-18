class Ghost:

    population = 0
    
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed                
	
    def getSpeed(self):
        return self.speed		
        
    def addGhost(self):        
        self.population += 1
        print("We have " + format(self.population) + " self.robots")
        
    @classmethod
    def addGhostClass(cls):
        cls.population += 4
        print("We have " + format(cls.population) + " cls.robots")
        
            

def createGhost(name, color, speed):
    g = Ghost(name, color, speed)
    return g


###########    
g2 = createGhost("G2", "blue", 400)
g2.addGhost()

g = createGhost("Ghost 1", "red", 60)
Ghost.addGhostClass()

