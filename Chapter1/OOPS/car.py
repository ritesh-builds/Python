class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"The name of Brand and Car is {self.brand} : {self.model}."

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_Safari = ElectricCar("TATA","Safari","65kWh")
print(my_Safari.brand)
print(my_Safari.model)
print(my_Safari.battery_size)
print(my_Safari.fullname())


my_car = Car("Toyota","Corolla-Altis")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname()) 

my_new_car = Car("TATA","Harrier")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.fullname()) 