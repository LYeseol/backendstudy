
class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start_engine(self):
        return "The engine is running"

class Car(Vehicle):
   def start_engine(self):
       return super().start_engine() + "It's a car engine."

my_car = Car("Kia", "Morning", "Blue")

print(my_car.make)
print(my_car.start_engine())