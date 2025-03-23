class Employee:
    def __init__(self,name, age, salary, exp):
        self.name = name
        self.age = age
        self.salary = salary
        self.experience =exp
        
    def v_detail1(self):
        print(f"name:{self.name}\nage:{self.age}\nsalary:{self.salary}\nexperience:{self.experience}")
        
        
        
class Admin(Employee):
    def __init__(self, name, age, salary, exp, dail_visitor):
        super().__init__(name, age, salary, exp)
        self.d_v=dail_visitor
        self.adsalary = 30000
        
    def v_detail2(self):
        print(f"name:{self.name}\nage:{self.age}\nsalary:{self.salary}\nexperience:{self.experience}\nDaily visit are{self.d_v}")
        
       
        
class Instructor(Employee):
    def __init__(self, name, age, salary, exp,subject,class_duration):
        super().__init__(name, age, salary, exp)
        self.subject = subject
        self.class_d = class_duration
        self.insalary = 50000
            
    def v_detail3(self):
        print(f"name:{self.name}\nage:{self.age}\nsalary:{self.salary}\nexperience:{self.experience}\nSubject:{self.subject}\nclass duration:{self.class_d}")
        
        
class Accountant(Employee):
    def __init__(self, name, age, salary, exp):
        super().__init__(name, age, salary, exp)
        self.acsalary=70000
        self.admin = Admin(name, age, salary, exp, dail_visitor=100)
        self.instructor = Instructor(name, age, salary, exp, subject="Mathematics", class_duration="2 hours")
        print(f"admin salary:{self.admin.adsalary}")
        print(f"instructor salary:{self.instructor.insalary}")
        print(f"accountant salary:{self.acsalary}")
        
        
nobject = Accountant("Alice Brown", 40, 50000, 10)

        
        
        
        