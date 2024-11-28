class Mammal:
    def __init__(self, type):
        self.type = type

    def give_birth(self):
        print(self.type +" does not lay eggs")

class Egglayer:
    def can_lay_eggs(self):
        return True

class Dog(Mammal):
    pass

class Platypus(Mammal):
    def give_birth(self):
        print(self.type + " is a Mammal that lay eggs")


dog = Dog("Dog")
platypus = Platypus("Platypus")

dog.give_birth()
platypus.give_birth()