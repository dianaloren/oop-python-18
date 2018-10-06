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
    
    # 5. Class method can be used as a factory function

# Creating the object
gh = Ghost("Casper", "red", 10)
print("{} has {} lives".format(gh.getName(), str(gh.lives)))     #instance accessing class variable
print("Ghost.lives: ", Ghost.lives)     #class accessing class variable
print("\n")

# 1. Let's say I want to increase one life in Casper
print("\n# 1. Let's say I want to change the amount of lives in Casper")
# ACHTUNG
Ghost.lives += 1
print("{} has {} lives".format(gh.getName(), str(gh.lives)))     #instance accessing class variable

# Now all ghosts will have 11 lives
gh1 = Ghost("Bob", "blue", 10)
print("{} has {} lives".format(gh1.getName(), str(gh1.lives)))     #instance accessing class variable

# 2. Let's try with the instance Casper
Ghost.lives = 10        #reset class variable
print("\n# 2. Let's try with the instance Casper")
gh.lives += 1
print("{} has {} lives".format(gh.getName(), str(gh.lives)))        #instance accessing class variable
print("{} has {} lives".format(gh1.getName(), str(gh1.lives)))      #instance accessing class variable
'''
# 3. Casper lost one life: use method 'reduceLife'
print("\n# 3. Casper lost one life: use method 'reduceLife'")
gh.reduceLife()
print("{} has {} lives".format(gh.getName(), str(gh.lives)))     #instance accessing class variable
'''
# 3. I changed my mind and want all Ghosts to have 15 lives  (Casper should have now 16 because he had one added)
# illustrates instance variable shadowing class variable
print("\n# 3. I changed my mind and want all Ghosts to have 5 lives more  (Casper should have now 20 because we added 5 already")
# Another way to do it is with the @classmethod
gh.doSomethingWithLives()
print("{} has {} lives".format(gh.getName(), str(gh.lives)))        #instance accessing class variable
print("{} has {} lives".format(gh1.getName(), str(gh1.lives)))      #instance accessing class variable

Ghost.doSomethingWithLives()
print("{} has {} lives".format(gh.getName(), str(gh.lives)))        #instance accessing class variable
print("{} has {} lives".format(gh1.getName(), str(gh1.lives)))      #instance accessing class variable

# 4. Can I access an instance method from the class? 
print("\n# 4. Can I access an instance method from the class? ")
Ghost.getName() 