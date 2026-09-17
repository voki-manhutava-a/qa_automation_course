print("1. Python Conditions and If statements")
print("\n1.1 If statements")
number = 15
if number > 0:
    print("The number is positive")
print("\n1.2 Boolean variables can be used directly in if statements without comparison operators.")
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
print("\n2 elif statement")
#The elif keyword allows you to check multiple expressions for True 
# and execute a block of code as soon as one of the conditions evaluates to True.
menu_timing = "Lunch"
if menu_timing == "Breakfast":
    print("Enjoy your breakfast!")
elif menu_timing == "Lunch":
    print("Enjoy your meal!")
elif menu_timing == "Dinner":
    print("Bon appétit!")
else:
    print("Wrong entry")
  
print("\n4. else statement")


#password = input('Enter password! ')
#if password == "123":
#    print("Correct password")
#else:
#    print("Incorrect Password")
print("\n5 Nested if-else statement")
print("\n 5.1 Find a greater number between two numbers")

num1 = 54
num2 = 33

if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is greater than', num2)
else:
    print(num1, 'is smaller than', num2)

print("\n5.2 Checking even or odd numbers")

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
  
print('Задача: Написать программу для учеников от двенадцати лет, которые учатся  по крайней мере в 7 классе. Доступ к ней тем, кто младше, надо запретить. ')

age = 13
grade = 8
if age >=12 and grade >=7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен. Ваш возраст:', age, 'Ваш класс:', grade)


print('Задача:Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.')

number = -999
if number >=100 and number <=999:
    print('Число является трёхзначным.')
elif number < 0:
    print('Число', number, 'не натуральное.')
else:
    print('Число', number, 'не является трёхзначным.')
    
print('Задача: Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.')

number_02 = 123
if number_02 >=100 and number_02 <=999:
    digit1 = number_02 // 100
    digit2 = number_02 // 10 % 10
    digit3 = number_02 % 10
    if digit1 != digit2 and digit1 != digit3 and digit2 != digit3:
        print('Число', number_02, 'имеет различные цифры.')
    else:
        print('Число', number_02, 'не имеет различных цифры.')
else:
    print('Число', number_02, 'не является трёхзначным.')
    
    
#number_02 = 1221
#if number_02 >=100 and number_02 <=999:
#    if number_02 // 100 != number_02 // 10 % 10 and number_02 // 10 % 10 != number_02 % 10 and number_02 // 100 != number_02 % 10:
#        print('Все цифры различны.')
#    else:
#        print('Не все цифры различны.')
#else:
#    print('Число не является трёхзначным.')
    



