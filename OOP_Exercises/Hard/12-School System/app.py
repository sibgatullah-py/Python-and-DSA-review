from school import *

class App:
    def __init__(self):
        self.running = True
        self.school = School("Gintama High School")
        
    def run(self):
        self.__welcome()
        while self.running:
            self.__menu()
            choice = input("\n -->").strip()
            self.__choice(choice)
            
    def __welcome(self):
        print("-"*30)
        print(f"Welcome to {self.school.name}")
        print("-"*30)
        
    def __menu(self):
        print(f"1. About Students\n2. About Teachers")
        
    def __choice(self,choice):
        self.rotation = True
        while self.rotation:
            if choice == '1':
                print(f"1.Add student\n2.Show all students\n3.Search student by ID\n4.Return")
                
                schoice = input("\n-->").strip()
                
                if schoice == '1':
                    name = input("Name: ")
                    age = input("Age: ")
                    grade = input("Grade: ")
                    roll = input("Roll: ")
                    student = Student(name,age,grade,roll)
                    self.school.add_student(student)
                    
                if schoice == '2':
                    self.school.show_students()
                    
                if schoice == '3':
                    id = input("ID: ")
                    self.school.search_student(id)
                    
                if schoice == '4':
                    self.rotation = False
                    
            if choice == '2':
                print(f"1.Add teacher\n2.Show all teachers\n3.Search teacher by ID\n4.Return")
                
                tchoice = input("\n-->").strip()
                
                if tchoice == '1':
                    name = input("Name: ")
                    subject = input("Subject: ")
                    teacher = Teacher(name,subject)
                    self.school.add_teacher(teacher)
                    
                if tchoice == '2':
                    self.school.show_teachers()
                    
                if tchoice == '3':
                    id = input("ID: ")
                    self.school.search_teacher(id)
                    
                if tchoice == '4':
                    self.rotation = False
            
        
        
        
        


if __name__ == "__main__":
    app = App()
    app.run()