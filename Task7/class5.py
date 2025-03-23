# class Animals:
#     def speak():
#         print("animals are speaking")
        
        
# class Cat(Animals):
#     def speak():
#         print("animals are speaking")        
        
# class Dog(Animals):
#     def speak():
#         print("animals are speaking")


# oneobj = [Cat(),Dog()]
# for animal in oneobj:
#     Animals.speak()




class Employee:
    def __init__(self,name, age):
        self.name = name
        self.__age =age
    def __details():
        print("Employee details")
        
    def set_age(self,a):
        if a>0:
            self.__age = a
        else:
            print("age is not valid")
        
    def get_age(self):
        print(f"the age is {self.__age}")


oneemp=Employee("Ahsan",22)
print(oneemp.get_age())