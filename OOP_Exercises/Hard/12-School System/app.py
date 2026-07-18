from school import *
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class App:
    def __init__(self):
        self.running = True
        self.school = School("Gintama High School")
        
    def run(self):
        clear_screen()                  
        self.__welcome()
        while self.running:
            clear_screen()              
            self.__welcome()           # So the title shows again
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
            clear_screen()              

            if choice == '1':
                print(f"1.Add student\n2.Show all students\n3.Search student by ID\n4.Edit student data\n5.Delete student\n6.Return")
                
                schoice = input("\n-->").strip()
                
                if schoice == '1':
                    clear_screen()      
                    name = input("Name: ")
                    age = input("Age: ")
                    grade = input("Grade: ")
                    roll = input("Roll: ")
                    student = Student(name,age,grade,roll)
                    self.school.add_student(student)
                    input("\nPress Enter to continue...")    
                    
                if schoice == '2':
                    clear_screen()      
                    self.school.show_students()
                    input("\nStudent Added...")    
                    
                if schoice == '3':
                    clear_screen()      
                    id = input("ID: ")
                    self.school.search_student(id)
                    input("\nPress Enter to continue...")    
                    
                if schoice == '4':
                    clear_screen()      
                    id = input("Enter id: ")
                    self.school.edit_student(id)
                    input("\nStudent Edited...")    
                    
                if schoice == '5':
                    clear_screen()      
                    id = input("Enter id: ")
                    self.school.delete_student(id)
                    input("\nStudent Deleted...")    
                                    
                if schoice == '6':
                    self.rotation = False
                    
            if choice == '2':
                print(f"1.Add teacher\n2.Show all teachers\n3.Search teacher by ID\n4.Edit teacher\n5.Delete teacher\n6.Return")
                
                tchoice = input("\n-->").strip()
                
                if tchoice == '1':
                    clear_screen()      
                    name = input("Name: ")
                    subject = input("Subject: ")
                    teacher = Teacher(name,subject)
                    self.school.add_teacher(teacher)
                    input("\nTeacher Added...")    
                    
                if tchoice == '2':
                    clear_screen()      
                    self.school.show_teachers()
                    input("\nPress Enter to continue...")    
                    
                if tchoice == '3':
                    clear_screen()      
                    id = input("ID: ")
                    self.school.search_teacher(id)
                    input("\nPress Enter to continue...")    
                    
                if tchoice == '4':
                    clear_screen()      
                    id = input("Enter id: ")
                    self.school.edit_teacher(id)
                    input("\nTeacher Edited...")    
                    
                if tchoice == '5':
                    clear_screen()      
                    id = input("Enter id: ")
                    self.school.delete_teacher(id)
                    input("\nTeacher Deleted...")    
                                    
                if tchoice == '6':
                    self.rotation = False


if __name__ == "__main__":
    app = App()
    app.run()