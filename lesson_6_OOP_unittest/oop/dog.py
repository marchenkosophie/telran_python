class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} is barking"

    def sleep(self):
        return f"{self.name} is sleeping"


dog1 = Dog("Bob")
dog2 = Dog("Alice")

print(dog1.bark())

print(dog2.sleep())