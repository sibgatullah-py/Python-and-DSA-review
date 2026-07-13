class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
        
    def show_details(self):
        print(f"Name: {self.name}\nSalary: ${self.salary}")
        
    def annual_salary(self):
        annual = self.salary*12
        print(f"Annual salary: ${annual}")
        
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
       
    def manage_team(self):
        print(f"{self.name} is managing {self.department} department")
        
em1 = Manager('Alice',70000,'IT')
em1.show_details()
em1.annual_salary()
em1.manage_team()