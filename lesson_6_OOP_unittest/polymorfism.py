class Cat:
    def make_sound(self):
        return "meow"



class Dog:
    def make_sound(self):
        return "woof"


animals = [Cat(),Dog()]
for animal in animals:
    print(animal.make_sound())


