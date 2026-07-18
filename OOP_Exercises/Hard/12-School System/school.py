from students import *
from teachers import *


class School:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
        
    def add_student(self,student):
        self.students.append(student)
        
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
        
    def show_students(self):
        for student in self.students:
            print(student)
            
    def show_teachers(self):
        for teacher in self.teachers:
            print(teacher)
     
    def search_student(self,id):
        for student in self.students:
            if id == student.id:
                print(student)
                
    def search_teacher(self,id):
        for teacher in self.teachers:
            if id == teacher.id:
                print(teacher)










    
     


'''
Version 3 (⭐⭐⭐ Advanced) pending...

Add:

1. @property for validation
2. Class variable for ID generation
3. @classmethod alternate constructors (e.g., from_dict)
4. ABC if multiple person types must implement common behavior
'''   