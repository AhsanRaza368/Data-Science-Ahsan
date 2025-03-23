class Employ:
    def __init__(self, name, age, salary, experience):
        self.name = name
        self.age = age
        self.salary = salary
        self. experience =experience
    def details(self):
        print(f" name: {self.name} \n age: {self.age} \n salary: {self.salary} \n experience {self.experience} ")
        
        
class Admin(Employ):
    def __init__(self, name, age, salary, experience, daily_visitor):
        super().__init__(name, age, salary, experience)
        self.dailyvisitor = daily_visitor
        
    def salaryall(self):
        adsalary = 200000
        
        print(f" daily visit are {self.dailyvisitor} \n admin salary is{adsalary} \n instructor salary is {50000} \n accountant salary is {30000}")
        
    def novisit(self):
        print(f"no of visit {self.dailyvisitor}") 
        
class Instructure(Employ):
    def __init__(self, name, age, salary, experience, subject,classduration):
        super().__init__(name, age, salary, experience)
        
        self.subject = subject
        self.classduration = classduration
        
    def show_detail(self):
        print(f"your subject is {self.subject} /n your class duration is {self.classduration}")
        
    
class accountant(Employ):
    def __init__(self, name, age, salary, experience):
        super().__init__(name, age, salary, experience)
        print(f"salary is {self.salary}")
        
        
newob = Admin("ahsan", 24 , 10000, 2)
print(newob.salaryall)