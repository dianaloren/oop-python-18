class Ghost():
    def __init__(self):
        self.name = "Bob"
        self.__color = "red"
        
    def getColor(self):
        return self.__color
        
g = Ghost()
#print(repr(g.__color))
print(getattr(g))
