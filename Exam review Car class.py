#object Oriented programming
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

Car1 = Car("Green", 5000)
Car2 = Car("Yellow", 10000)                          

print(f" The {Car1.color} car has {Car1.mileage:,} miles. ")
print(f" The {Car2.color} car has {Car2.mileage:,} miles. ")


