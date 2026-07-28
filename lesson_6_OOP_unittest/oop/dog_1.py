class Dogs:
    species = 'Canis familiaris'
    def __init__(self, name):
        self.name = name


dog1 = Dogs("Bobby")
dog2 = Dogs("Julia")

print(dog1.species, dog1.name)
print(dog2.species, dog2.name)


Dogs.species = 'Mouse'

print(dog1.species, dog1.name)
print(dog2.species, dog2.name)



class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "..."


class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"


dog = Dog("Rex")
cat = Cat("Taki")

print(dog.name, "says: ", dog.make_sound())
print(cat.name, "says: ", cat.make_sound())


class Fish(Animal):
    pass

fish = Fish("Nemo")
print(fish.name, "says: ", fish.make_sound())



