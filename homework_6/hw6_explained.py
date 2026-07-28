class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"{self.name} works as {self.position} and earns {self.salary}"


employee1 = Employee("Anna", "Qa Engineer", 18000)

employee2 = Employee("Tom", "Backend Developer", 20000)

print(employee1.get_info())
print(employee2.get_info())


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            return "Not enough products"
        self.quantity -= amount
        return None


laptop = Product("Laptop", 100, 5)



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


vehicle1 = Vehicle()
car = Car()
bicycle = Bicycle()
print(vehicle1.move())
print(car.move())
print(bicycle.move())


class User:
    country = "Israel"

    def __init__(self, username, age):
        self.username = username
        self.age = age

user1 = User("Inna", 30)
user2 = User("Tom", 25)
user3 = User("Kate", 28)

print(user1.country, user2.country, user3.country)


User.country = "Canada"

print(user1.country, user2.country, user3.country)