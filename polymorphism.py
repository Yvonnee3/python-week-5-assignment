class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print("Driving")
class Plane(Vehicle):
    def move(self):
        print("Flying")


Vehicles = [Car(), Plane()]
for vehicle in Vehicles:
    vehicle.move()