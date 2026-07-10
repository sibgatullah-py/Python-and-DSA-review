class Student:
    collage = "GAI" # class attribute common for every object
    def __init__(self,name,roll,marks):# object attribute different according to objects
        self.name = name
        self.roll = roll
        self.marks = marks
        
    def welcome(self):
        print("welcome student,",self.name)
        
    def get_marks(self):
        return self.marks
        

s1 = Student("Roger",6,68)
s2 = Student("Benedetta",3,85)
s3 = Student("Bruno",10,75)
s4 = Student("Brody",21,73)

print(s1.name,s1.roll,s1.get_marks())
print(s2.name,s2.roll,s2.marks)
print(s3.name,s3.roll,s3.marks)
print(s4.name,s4.roll,s4.marks,s4.collage)

s1.welcome()