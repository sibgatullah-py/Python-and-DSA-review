from itertools import count

class Student:
    _id_counter = count(1)
    
    def __init__(self,name,age,grade,roll):
        self.id = next(self._id_counter)
        self.name = name
        self.age = age
        self.grade = grade
        self.roll = roll
        
    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nRoll: {self.roll}"
    