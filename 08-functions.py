print('Functions')
print('Exercise 1. Create a Function with Parameters. Write a function called demo() that accepts two parameters: a name and an age. The function should print these values directly to the console.')
#name = "Kelly"
#age = 25
def demo(name, age):
    print(name, age)
demo('Kelly', 25)

print('Exercise 2. Variable Length of Arguments (*args) \n Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error.')

def func1(*args):
    print('Printing values:')
    for i in args:
        print(i)
func1(80, 100, 120, 90)

print('Exercise 3. Return Multiple Values from a Function \n Write a function calculation() that accepts two variables and calculates both addition and subtraction. The function must return both results in a single return statement.')

def calculation(a, b):
    # print(f'Addition: {a + b} \nSubstraction: {a - b}')
    add = a + b
    sub = a - b
    return add, sub

add, sub = calculation(40, 20)
print(add, sub)

print('Exercise 4. \nНапишите функцию draw_box(), которая выводит звёздный прямоугольник c размерами 10 x 15')
def draw_box(height, length, symbol):
    for i in range(height):
        if i == 0 or i == height - 1:
            print(symbol * length)
        else:
            print(symbol + ' ' * (length - 2) + symbol)
draw_box(15, 10, '*')
print('Exercise 6. Generate a List of Even Numbers (Range Function)\nCreate a function that generates a list of all even numbers between 4 and 30. ')

def num_list_1(start, end):
    lst = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            lst.append(i)
    return lst
print(num_list_1(4, 30))
            
            
def num_list_2(start, end):
    return list(range(start, end + 1, 2))
                
print(num_list_2(4, 30))

print('Exercise 7. \nFind the Largest Item in a List. \nCreate a function that takes a list of numbers as input and returns the largest item from that list without using the built-in max() function')
def max_value(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest


number_list = [4, 6, 8, 24, 12, 222]
print(max_value(number_list))

print('Exercise 8. \nНапишите функцию, которая принимает три параметра (имя, фамилия, отчество) и выводит на печать ФИО - инициалы')

def print_fio(name, surname, patronymic):
    full_name = f'{surname} {name[0].upper()}.{patronymic[0].upper()}.'
    print(full_name)

print_fio('Александр', 'Пушкин', 'Сергеевич')
    

    
print('Exercise 9. \nНапишите функцию print_case_counts(s), которая принимает на вход строку s и выводит для неё текст - количество букв в верхнем и нижнем регистрах соответственно')

def print_case_counts(s):
    upp = 0
    low = 0
    for i in s:
        if i.islower():
            low += 1
        elif i.isupper():
            upp += 1
    print('Строчных букв:', low)
    print('Заглавных букв:', upp)

text = 'aPn3!biuU'

print_case_counts(text)

print('Exercise 10. \nCall Function using Positional and Keyword Arguments \nDefine a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function twice: once using positional arguments and once using keyword arguments.')

def describe_pet(animal_type, pet_name):
    print("I have a", animal_type)
    print("My", animal_type + "'s name is", pet_name)

describe_pet("dog", "Buddy")
describe_pet(pet_name="Willie", animal_type="parrot")

print('Exercise 11. Create a Function with Keyword Arguments\nCreate a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.')

def print_info(**person):
    # for i in person:
    #     print(i,':', person.get(i, 0))
    for key, value in person.items():
        print(f'{key}: {value}')
        
# Expected Output:
# name: Alice
# age: 30
# city: New York
    
print_info(name="Alice", age=30, city="New York")

print('\nExercise 12. Modifying Global Variables.\nDefine a global variable global_var = 10. Write a function that successfully changes the value of this global variable to 20.')

global_var = 10
def change():
    global global_var
    global_var = 20
   
print(f'Initial variable: {global_var}') 
change()
print(f'Modified variable: {global_var}')

print('\nDefault parameter value and docstring')
def greet(name, greeting='Hello'):
    """Return a greeting for the given name."""
    return f'{greeting}, {name}!'

print(greet('Kelly'))
print(greet('Kelly', 'Hi'))

print('\nDifference between print and return')
def greet_print(name):
    print(f'Hello, {name}!')

result_print = greet_print('Kelly')
print(result_print)
result_return = greet('Kelly')
print(result_return.upper())