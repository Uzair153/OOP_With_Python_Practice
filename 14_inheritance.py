# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Vehicle is being driven.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")

# Grandchild class inheriting from Car
class SportsCar(Car):
    def drive(self):
        print("Sports car is being driven at high speed.")

# Create instances of each class
vehicle = Vehicle("Generic")
car = Car("Toyota")
sports_car = SportsCar("Ferrari")

# Call the drive method on instances
vehicle.drive()      
car.drive()          
sports_car.drive()   
