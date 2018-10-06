class PacDot:
	
	def __init__(self, size=10, score=10):
		self._size = size
		self._score = score

	def getScore(self):
		return self._score
	
	def getSize(self):
		return self._size	
    
    def blink(self):
        print("this is blinking")
    
    
class PowerPellet(PacDot):
    
    def __init__(self, size=25, score=50):
        PacDot.__init__(self, size, score)
        self._sizeModifier = -2
        
    def blink(self):
        self._size += self._sizeModifier
        if self._size < 10 or self._size > 20:
            self._sizeModifier = - self._sizeModifier
            print("size: ", self._sizeModifier)

pd = PacDot()        
print(pd.getScore())
print(pd.getSize())

pp = PowerPellet()
print(pp.blink())
