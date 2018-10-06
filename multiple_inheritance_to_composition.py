class Learner:
    def __init__(self):
        self.classes = []   #classes the learner takes
        
    def enroll(self, course):
        self.classes.append(course)
        
    def getEnrollments(self):
        return self.classes
    
    def show(self):
        print("This is Learner")
        
class Teacher:
    def __init__(self):
        self.classes = []    #classes the teacher gives
        
    def teach(self, course):
        self.classes.append(course)
        
    def getCourses(self):
        return self.classes
    
    def show(self):
        print("This is Teacher")
        
# composed by both Learner and Teacher
class Person:     
    def __init__(self, name, surname, idnumber):
        self.name = name
        self.surname = surname
        self.idnumber = idnumber
        
        #we use parts of Teacher and Learner
        self.teacher = Teacher()
        self.learner = Learner()
        
    def getName(self):
        return self.name
        
    def setName(name):
        self.name = name
        
    def getClassesLearner(self):
        return self.learner.getEnrollments()
    
    def addClassesLearner(self, course):
        self.learner.enroll(course)
       
    def getClassesTeacher(self):
        return self.teacher.getCourses()
        
    def addClassesTeacher(self, course):
        self.teacher.teach(course)

        
# instantiate Person
p1 = Person("Jane", "Fonda", "1224A")
print(p1.getName())
p1.addClassesLearner("Math")
p1.addClassesTeacher("Geometry")
print("{} teaches {}, and attends {}".format(p1.getName(), p1.getClassesTeacher(), p1.getClassesLearner()))