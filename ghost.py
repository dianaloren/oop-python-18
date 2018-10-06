class Ghost:
	def __init__(self, name, color, speed):
		self.name = name
		self._color = color
		self.__speed = speed
	
	def getSpeed(self):
		return self.__speed
		
def getSpeed(ghost):
	return ghost.getSpeed()
		
ghosts = []
g = Ghost("Bob", "red", 60)
ghosts.append(g)
g2 = Ghost("G2", "blue", 400)
ghosts.append(g2)

print(dir(g))

# getting Speed
print("Speed: ", g.getSpeed())
print("Speed: ", getSpeed(g2))
print("Speed: ", g.__speed)     #__speed is rewritten as _Ghost__speed   --> this line will return error
print("Speed: ", getSpeed(g2))


print(ghosts[0]._color)