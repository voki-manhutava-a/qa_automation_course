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

res = calculation(40, 20)
print(res)

print('Напишите функцию draw_box(), которая выводит звёздный прямоугольник c размерами 10 x 15')
height = 14
lenght = 10
a = '*'
def rectangle():
    for i in range(height):
        if i == 0 or i == 13:
            print(a * 10)
        else:
            print(a+' '*8+a)
rectangle()
print('Exercise 6. Generate a List of Even Numbers (Range Function)\nCreate a function that generates a list of all even numbers between 4 and 30. ')

def num_list_1(num):
    lst = []
    for i in range(2, num + 1):
        if i % 2 == 0:
            lst.append(i)
    return lst
print(num_list_1(30))
            
            
def num_list_2():
    return list(range(2, 30, 2))
                
print(num_list_2())

print('Exercise 7. \nFind the Largest Item in a List. \nCreate a function that takes a list of numbers as input and returns the largest item from that list without using the built-in max() function')
def max_value(numbers):
    max_of_rest = numbers[0]
    for i in numbers:
        if i > max_of_rest:
            max_of_rest = i
    return max_of_rest


x = [4, 6, 8, 24, 12, 222]
print(max_value(x))

print('Exercise 8. \nНапишите функцию, которая принимает три параметра (имя, фамилия, отчество) и выводит на печать ФИО - инициалы')

def print_fio(name, surname, patronymic):
    full_name = (surname[0] + name[0] + patronymic[0]).upper()
    print(full_name)

print_fio('Александр', 'Пушкин', 'Сергеевич')
    

    
print('Exercise 8. \nНапишите функцию print_case_counts(s), которая принимает на вход строку s и выводит для неё текст - количество букв в верхнем и нижнем регистрах соответственно')

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

s = 'aPn3!biuU'

print_case_counts(s)

print('Exercise 10. \nCall Function using Positional and Keyword Arguments \nDefine a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function twice: once using positional arguments and once using keyword arguments.')

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
my_function(name="Willie", animal="parrot")

print('Exercise 11. Create a Function with Keyword Arguments\nCreate a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.')

def print_info(**person):
    # for i in person:
    #     print(i,':', person.get(i, 0))
    for item in person.items():
        key = item[0]
        value = item[1]
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