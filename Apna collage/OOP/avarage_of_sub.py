class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        average = sum/len(self.marks)
        print(self.name," got average of ",average)
        
        
s1 = Student('Ayato',[86,84,88])
s1.avg()