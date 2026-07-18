from students import *
from teachers import *


class School:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    
    #Student methods    
    def add_student(self,student):
        self.students.append(student)
        
    def show_students(self):
        for student in self.students:
            print(student)
            print("\n")
            
    def search_student(self,ID):
        id = int(ID)
        for student in self.students:
            if id == student.id:
                print(student)
                
    def delete_student(self,ID):
        id = int(ID)
        for index,student in enumerate(self.students):
            if id == student.id:
                self.students.pop(index)
                
                
    #Teacher methods
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
              
    def show_teachers(self):
        for teacher in self.teachers:
            print(teacher)
            print("\n")
                
    def search_teacher(self,ID):
        id = int(ID)
        for teacher in self.teachers:
            if id == teacher.id:
                print(teacher)
                             
    def delete_teacher(self,ID):
        id = int(ID)
        for index,teacher in enumerate(self.teachers):
            if id == teacher.id:
                self.teachers.pop(index)










    
     


'''
Version 3 (⭐⭐⭐ Advanced) pending...

Add:

1. @property for validation
2. Class variable for ID generation
3. @classmethod alternate constructors (e.g., from_dict)
4. ABC if multiple person types must implement common behavior
'''   