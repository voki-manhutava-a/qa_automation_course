print('Exercise 1: Define an Empty Vehicle Class. \n Problem Statement: Write a Python program to create a class named Vehicle that has no variables or methods defined inside it.')
class Vehicle:
    '''I have created a new class Vehicle'''
print(Vehicle)

print('\nExercise 2: Vehicle Class with Instance Attributes\n Problem Statement: Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.')
class Vehicle:
    def __init__(self,  max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle( 250, 18)
print(f" Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")

print('\nExercise 3: Rectangle Class with Area & Perimeter\n Problem Statement: Write a Python program to create a Rectangle class with length and width as instance attributes, and two methods: area() that returns the area and perimeter() that returns the perimeter.')
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.width+self.length) * 2
rectangle = Rectangle(35, 12)
print(f'Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}')

print('\nExercise 4: Student Class with Average Grade\n Problem Statement: Write a Python program to create a Student class that stores a student’s name and a list of marks. Add a method average() that calculates and returns the average of all marks.')

class Student:
    def __init__(self, st_name, st_marks):
        self.st_name = st_name
        self.st_marks = st_marks
    def average(self):
        return sum(self.st_marks) / len(self.st_marks)
    
s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f'Average mark of a student is {s1.average()}')

print('\nExercise 5: Product Class with Stock Value Calculator\n Problem Statement: Write a Python program to create a Product class with three instance attributes: name, price, and quantity. Add a method total_value() that returns the total stock value by multiplying price by quantity.')
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity
p1 = Product("Laptop", 899.99, 5)
print(f'Total stock value of {p1.name} is ${p1.total_value()}')

print('\nExercise 6: User Class with Password Validation\n Problem Statement: Write a Python program to create a User class that stores a username and a password. Add a check_password(input_password) method that returns True if the input matches the stored password, and False otherwise.')
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def check_password(self, input_psw):
        return self.password == input_psw
u1 = User("alice", "secure123")
print(u1.check_password('secure123'))
print(u1.check_password('secure1234'))

print('\nExercise 7: Coffee Machine with Multi-Resource Tracking\n Problem Statement: Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.')
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_latte(self):
        water_needed = 200
        coffee_needed = 20
        milk_needed = 150
        if self.water >= water_needed and self.coffee >= coffee_needed and self.milk >= milk_needed:
            self.water -= water_needed
            self.coffee -= coffee_needed
            self.milk -= milk_needed
            print(f'Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml')
        else:
            print('Not enough resources to make a latte.')
        
machine = CoffeeMachine(water=300, coffee=100, milk=200)
machine.make_latte()
machine.make_latte()