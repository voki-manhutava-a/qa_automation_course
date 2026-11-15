


print("1. Python while loop")

print("\n1.1 Run loop till count is less than or equal to 3")
count = 1
while count <= 3:
    print(count)
    count = count + 1  

print("\n1.2 Check how many times a given number can be divided by 3 before it is less than or equal to 10")
start_number = 100  # keep the initial value, the loop changes 'number'
number = start_number
iterations = 0
# '//' is floor division, so number stays an int: 100 -> 33 -> 11 -> 3
while number > 10:
    number = number // 3
    iterations += 1
print("Start number:", start_number, "| final number:", number)  # 100 | 3
print("Total iterations required:", iterations)  # 3

print("\n1.3 Ask the user to enter a number between 100 and 500. We will keep asking the user to enter a correct input until he/she enters the number within a given range.")
# The code below has to be uncommented and run in the terminal, because it requires input.
# while-else: the 'else' block runs only if the loop finished WITHOUT 'break'.
# There is no 'break' here, so 'else' runs once the entered number is correct.

# user_number = int(input("Enter any number between 100 and 500 "))
# while user_number < 100 or user_number > 500:
#     print("Incorrect number, please enter correct number:")
#     user_number = int(input("Enter a number between 100 and 500 "))
# else:
#     print("Given number is correct", user_number)

print("\n2. If-else in while loop")
print("2.1 Print even and odd numbers from 1 to the entered number")
limit = 15
current = 1
while current <= limit:
    if current % 2 == 0:
        print(current, "- it's an even number")
    else:
        print(current, "- it's an odd number")
    current += 1

print("\n3. Break in while loop")
print("3.1 Write a while loop to display each character from a string and if a character is a number, then stop the loop")
login = "Jesaa29Roy"
login_size = len(login)
pos = 0
while pos < login_size:
    if login[pos].isdecimal():
        break
    print(login[pos], end=" ")
    pos += 1
print()  # J e s a a

print("\n4. Continue statement")
print("4.1 Write a while loop to display only alphabets from a string")
# The counter is increased at the end of the loop body, so 'continue' is not needed:
# it is enough to check 'isalpha()'
nickname = "Jesaa29Roy"
nickname_size = len(nickname)
idx = 0
while idx < nickname_size:
    if nickname[idx].isalpha():
        print(nickname[idx], end=" ")
    idx += 1
print()  # J e s a a R o y

print("\n5. Nested while loops")
print("5.1 Use nested while loop to print a pattern")
asterisk = "*"
row = 1
while row <= 5:
    column = 0
    while column < row:
        print(asterisk, end=" ")
        column += 1
    print()  
    row += 1

# The task had this example, it works without a nested loop:
# row = 1
# while row <= 5:
#     print("* " * row)
#     row += 1

print('5.2 Цифровым корнем числа n называется число, получающееся следующим образом: вычисляется сумма цифр числа n затем сумма цифр у получившегося числа и так далее, пока не получится однозначное число.  Например, цифровой корень числа 9875 равен 2. Напишите программу, которая находит цифровой корень данного числа')

number = 1208
input_number = 1208
while number >= 10:
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    number = digit_sum
print('\n Цифровой корень числа', input_number, 'равен', number)




print("\n6. Task: print numbers from 1 to n, except 5-15, 17-37 and 78-87")
#На вход программе подаётся натуральное число. Напишите программу, которая выводит числа от 1 до n
# включительно за исключением: чисел от 5-15 17-37 78-87

# n = 20 (the last number is inside the first range), n = 90 (all three ranges)
for n in [20, 90]:
    print("n =", n)
    current = 1
    while current <= n:
        if not (5 <= current <= 15 or 17 <= current <= 37 or 78 <= current <= 87):
            print(current, end=" ")
        current += 1
    print()