class Person:
    def __init__(self, name, surname, idnumber):
        self.name = name
        self.surname = surname
        self.idnumber = idnumber
        
    def getName(self):
        return self.name
        
    def setName(name):
        self.name = name
         
class Learner:
    def __init__(self):
        self.classes = ["learner"]   #classes the learner takes
       
    def enroll(self, course):
        self.classes.append(course)
        
    def getEnrollments(self):
        return self.classes
    
    def show(self):
        print("This is Learner")
        
class Teacher:
    def __init__(self):
        self.classes = ["teacher"]    #classes the teacher gives
        
    def teach(self, course):
        self.classes.append(course)
        
    def getCourses(self):
        return self.classes
    
    def show(self):
        print("This is Teacher")
        
# inherit from both Learner and Teacher
class Tutor(Person, Learner, Teacher):
    
    def __init__(self, *args, **kwargs):
        Person.__init__(self, *args, **kwargs)
        Learner.__init__(self)
        Teacher.__init__(self)
    
    
    def getClassesToAttend(self):
        return self.classes
    
    def addClassesToAttend(self, course):
        self.enroll(course)
       
        
tutor1 = Tutor("Jane", "Fonda", "1234A")
tutor1.show()
print(dir(tutor1))

#learner
tutor1.addClassesToAttend("Language1")
print(tutor1.getEnrollments())
#teacher
tutor1.teach("Math1")
print(tutor1.getCourses())

#tutor1.showLearner()
tutor1.addClassesToAttend("Language")
print(tutor1.getClassesToAttend())
tutor1.enroll("Math")
tutor1.teach("Programming")
print(tutor1.getEnrollments())
print(tutor1.getCourses())       

tutor2 = Tutor("Bob", "Bobby", "123ACB")
tutor2.enroll("Math")
tutor2.teach("Languages")    
print(tutor2.getEnrollments()) 
