class Employee:
    def __init__(self, name, age, salary, exp):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience = exp
        
    def v_detail1(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\nExperience: {self.experience}")
        
        
class Admin(Employee):
    def __init__(self, name, age, salary, exp, dail_visitor):
        super().__init__(name, age, salary, exp)
        self.d_v = dail_visitor
        self.adsalary = 30000  # Specific salary for Admin
        
    def v_detail2(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\nExperience: {self.experience}\nDaily Visitors: {self.d_v}")
        
        
class Instructor(Employee):
    def __init__(self, name, age, salary, exp, subject, class_duration):
        super().__init__(name, age, salary, exp)
        self.subject = subject
        self.class_d = class_duration
        self.insalary = 50000  # Specific salary for Instructor
            
    def v_detail3(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\nExperience: {self.experience}\nSubject: {self.subject}\nClass Duration: {self.class_d}")
        
        
class Accountant(Employee):
    def __init__(self, name, age, salary, exp):
        super().__init__(name, age, salary, exp)
        self.acsalary = 70000  # Specific salary for Accountant
        
        # Create instances of Admin and Instructor
        self.admin = Admin(name, age, salary, exp, dail_visitor=100)  # Example value for daily_visitor
        self.instructor = Instructor(name, age, salary, exp, subject="Mathematics", class_duration="2 hours")  # Example values
        
        # Display salaries
        print(f"Admin Salary: {self.admin.adsalary}")
        print(f"Instructor Salary: {self.instructor.insalary}")
        print(f"Accountant Salary: {self.acsalary}")
        

# Create an instance of Accountant
nobject = Accountant("Alice Brown", 40, 50000, 10)