class Door:
    keycode = "0101"
    
    def __init__(self, number, status, color="gray", locked=False):
        self.number = number
        self.status = status
        self.color = color
        self.locked = locked 
        
    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(self.__class__.__name__, self.number, self.status, self.color,self.locked)
        
    def describe(self):
        return "{}, {}, {}, {}, {}".format(self.number, self.status, self.color,self.locked, self.keycode)

    def paint(self, color):
        self.color = color
        print("New color is: ", color)
        
# Inheritance        
class SecurityDoor(Door):
    def __init__(self, number, status):
        Door.__init__(self, number, status)
        self.number = number
        self.status = status

# Composition
class ComposedDoor:
    def __init__(self, number, status):
        self.number = number
        self.status = status
        self.door = Door(self.number, self.status)
    
    def __getattr__(self, attr):
        return getattr(self.door, attr)
        
    def describe(self):
        #return self.door.describe()
        return self.door.keycode
        
    def getKeyCode(self):
        print(self.keycode)
        
door = Door(1, "closed")     
print(repr(door)) 
print(door.describe())

cdoor = ComposedDoor(2, "closed")
print(cdoor.describe())

cdoor.getKeyCode()
  
















