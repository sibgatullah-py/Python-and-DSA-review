from itertools import count

class Teacher:
    _id_counter = count(1)
    
    def __init__(self,name,subject):
        self.id = next(self._id_counter)
        self.name = name
        self.subject = subject
        
    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nSubject: {self.subject}"