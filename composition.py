class Door:
    keycode = "0101"
    
    def __init__(self, number, status, color="gray", locked=False):
        self.number = number
        self.status = status
        self.color = color
        self.locked = locked

    def __repr__(self):
        return '{},{},{},{},{}'.format(self.__class__.__name__,self.color, self.locked, self.number, self.status)
        
    def describe(self):
        return "{},{},{},{}".format(self.color, self.locked, self.keycode, self.status)      
        
    def paint(self, color):
        self.color = color
        print("New color is: ", self.color)
        
  
        
class SecurityDoor(Door):
    
    def __init__(self, number, status):
        Door.__init__(self, number, status)
        self.number = number
        self.status = status
        
class ComposedDoor:
    
    def __init__(self, number, status):
        self.number = number
        self.status = status
        self.door = Door(number, status)    #composition: creates an instance of an object and USES its properties
    '''        
    def __getattr__(self, attr):        
        return getattr(self.door, attr)
    '''   
    def describe(self):
        return self.door.describe()
        
    def foo(self):
        print(repr(self.door))
        
    def getKeyCode(self):        
        print(self.keycode)
        
    
d = Door(1, "closed")
print("Door: " + d.describe())
d.paint("blue")    
print("Door: "+ d.describe())

sd = SecurityDoor(5, "open")
print("Security Door: " +sd.describe())

cd = ComposedDoor(11, "broken")
print("Composed Door: " +cd.describe())
#cd.foo()
cd.getKeyCode()