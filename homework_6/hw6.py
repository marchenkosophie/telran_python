class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_info(self):
        print(f"{self.name} works as {self.position} and earns {self.salary}")


emma = Employee("Emma", "nurse", 10000)
katherine = Employee("Katherine", "teacher", 15000)

emma.get_info()
katherine.get_info()

print()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return None
        return "Not enough products"



laptop = Product("Laptop", 2048, 5)

print(laptop.buy(2))
print("Remaining balance after purchase 2 шт:", laptop.quantity)
print(laptop.buy(10))
print("The balance has not changed.:", laptop.quantity)



print()


class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding"


print()


class User:
    country = "Israel"
    def __init__(self, username, age):
        self.username = username
        self.age = age



bonnie = User("Bonnie", 18)
rebecca = User("Rebecca", 24)
elena = User("Elena", 30)


print(rebecca.country)
print(bonnie.country)
print(elena.country)

User.country = "Canada"


print(rebecca.country)
print(bonnie.country)
print(elena.country)