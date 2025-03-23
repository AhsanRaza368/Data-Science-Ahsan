# class Voucher:
#     def __init__(self,name,balance,voucher_code,per_of_discount):
#         self.__name = name
#         self.__balance = balance
#         self.__voucher_code =voucher_code
#         self.__per_of_discount =per_of_discount
        
        
#     def set_name(self,nm):
#         if len(nm) >=4:
#             self.__name=nm
#         else:
#             print("you enter uinvalid name")
            
            
#     def get_name(self):
#         print(f"you name is {self.__name}")
        
        
#     def set_balance(self,b):
#         if b>0:
#             self.__balance=b
#         else:
#             print("insufficient balance")
            
#     def get_balance(self):
#         print(f"your balance is:{self.__balance}")
        
#     def set_voucher_code(self,vc):
#         if vc>=0:
#             self.__voucher_code=vc
#         else:
#             print(f"your voucher code is invalid")
            
#     def get_voucher_code(self):
#         print(f"your voucher code is:{self.__voucher_code}")
        
#     def set_percentage_od_discount(self,pod):
#         if pod>0:
#             self.__per_of_discount=pod
#         else:
#             print("no discount")
            
#     def get_percentage_od_discount(self):
#         print(f"you get discount:{self.__per_of_discount}")
        
        
        
# nobj = Voucher("ahsan",10000,5555,10)
# print(nobj.set_name("ahsan raza"))


#TASK1


# class Voucher:
#     def __init__(self, name, balance, voucher_code, per_of_discount):
#         self.__name = name
#         self.__balance = balance
#         self.__voucher_code = voucher_code
#         self.__per_of_discount = per_of_discount

#     def set_name(self, nm):
#         if len(nm) >= 3: 
#             self.__name = nm
#         else:
#             print("You entered an invalid name")

#     def get_name(self):
#         print(f"Your name is {self.__name}")

#     def set_balance(self, b):
#         if b > 0:
#             self.__balance = b
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         print(f"Your balance is: {self.__balance}")

#     def set_voucher_code(self, vc):
#         if vc >= 0:
#             self.__voucher_code = vc
#         else:
#             print("Your voucher code is invalid")

#     def get_voucher_code(self):
#         print(f"Your voucher code is: {self.__voucher_code}")

#     def set_percentage_of_discount(self, pod):
#         if pod > 0:
#             self.__per_of_discount = pod
#         else:
#             print("No discount available")

#     def get_percentage_of_discount(self):
#         print(f"You get a discount of: {self.__per_of_discount}%")

# nobj = Voucher("ahsan", 10000, 5555, 10)
# nobj.set_name("Ahsan Raza")
# nobj.get_name()
# nobj.set_balance(2000)
# nobj.get_balance()







#TASK2
#RNd protected (use to access within derived class )
# Base class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name        
#         self._salary = salary    

#     def show_details(self):
#       
#         print(f"Employee: {self.name}, Salary: {self._salary}")

# # Derived class (subclass)
# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)  
#         self._bonus = bonus            

#     def show_manager_details(self):
#        
#         print(f"Manager: {self.name}, Salary: {self._salary}, Bonus: {self._bonus}")

#     def increase_salary(self, amount):
#        
#         self._salary += amount  
#         print(f"Updated Salary: {self._salary}")


# manager = Manager("Alice", 70000, 5000)

# manager.show_manager_details() 
# manager.increase_salary(300)
# print(manager._salary)
# print(manager._bonus)






#task3

# class Shape:
#     def corner(self):
#         print("All shapes contain specific corners")
        
# class Circle(Shape):
#     def corner(self):
#         print("It has no corners")
  
# class Triangle(Shape):
#     def corner(self):
#         print("It contains 3 corner points")
        
# newobj = [Circle(), Triangle()]

# for n in newobj:
#     n.corner()




# from abc import ABC, abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def details(self,name,age):
#         pass
    
# class Suzuki(Car):
#     def start(self):
#         print("suzuki has been start")
        
#     def details(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"car name is: {self.name}\ncar age is:{self.age}")
        
        
# class Tesla(Car):
#     def start(self):
#         print("Tesla has been start")
        
#     def details(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"car name is: {self.name}\ncar age is:{self.age}")
        
        

# carone = Suzuki()
# carone.details("ahsan",20)