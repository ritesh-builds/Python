class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        self.__brand = brand   
        Car.total_car += 1

    def chai_brand(self):
        return self.__brand + "!"    

    def fullname(self):
        return f"The name of Brand and Car is {self.brand} : {self.__model}."

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are mean of transport."
    
    @property
    def model(self):
        return self.__model

    # FIX: Adding a setter so you can change the model name
    @model.setter
    def model(self, value):
        self.__model = value

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

# --- Execution ---

my_Safari = ElectricCar("TATA", "Safari", "65kWh")
print(f"Brand name is: {my_Safari.brand}")
print(f"Model name is: {my_Safari.model}")
print(f"The size of Battery is: {my_Safari.battery_size}")
print(f"{my_Safari.fullname()}")
print(my_Safari.chai_brand())
print(f"Fuel type is: {my_Safari.fuel_type()}")
print(f"Total cars are: {Car.total_car}") # Recommended to use Class name for static variables

my_car = Car("Toyota", "Corolla-Altis")
print(f"Brand name is: {my_car.brand}")
print(f"Model name is: {my_car.model}")
print(f"{my_car.fullname()}") 
print(f"{my_car.general_description()}")  

# Yeh ab kaam karega kyunki humne @model.setter add kar diya hai
my_car.model = "Glanza"
print(f"Updated Model: {my_car.model}")

my_new_car = Car("TATA", "Harrier")
print(f"Brand name is: {my_new_car.brand}")
print(f"Model name is: {my_new_car.model}")
print(f"{my_new_car.fullname()}")

nexon = Car("TATA","Nexon")
print(f"Brand name is: {nexon.brand}")
print(f"Model name is: {nexon.model}")
print(f"{nexon.fullname()}")
print(f"Fuel type is: {nexon.fuel_type()}")

print(f"Total cars: {Car.total_car}") 
