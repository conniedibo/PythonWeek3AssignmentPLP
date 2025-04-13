# Parent class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

# Child class: Car
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road 🚗")

# Child class: Plane
class Plane(Vehicle):
    def move(self):
        print("Plane is flying in the sky ✈️")

# Child class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is pedaling on the path 🚲")

# Child class: Boat
class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on the water 🛳️")

# Test polymorphism
vehicles = [Car(), Plane(), Bicycle(), Boat()]

for vehicle in vehicles:
    vehicle.move()
