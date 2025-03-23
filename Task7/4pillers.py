class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Engine started!"
    def view1(self):
        print(f"brand name is: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def view(self):
        print(f"your model is: {self.model}")

my_car = Car("Suzuki","2018")
my_car.view()
