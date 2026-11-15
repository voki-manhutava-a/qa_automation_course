# Loops for
set_1 = {19, 23, 25, 29, 31}
for i in set_1:
    print("Value of i is:", i)

# Print sum of all even numbers from 10 to 20
even_sum = 0
for i in range(10, 21, 2):
    even_sum = even_sum + i
print('Sum of even numbers from 10 to 20:', even_sum)

# Calculate the square of each number of list
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    square = i ** 2
    print('Value of square of', i, 'is:', square)

# Calculate the average of list of numbers
numbers_avg = [10, 20, 30, 40, 50]
total = 0
for i in numbers_avg:
    total += i
average = total / len(numbers_avg)
print('Average:', average)

print('\n If-else in for loop')

# Print all even and odd numbers
for i in range(1, 10):
    if i % 2 == 0:
        print(i, 'is an even number')
    else:
        print(i, 'is an odd number')

# Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
divisible_by_2 = []
for i in range(9, 51):
    if i % 2 == 0:
        divisible_by_2.append(i)
print('The list of the divisible numbers from the range is:', divisible_by_2)

# подсчитать количество чисел из диапазона от 1 до 100 (включительно), квадрат которых оканчивается на 4
counter = 0
for i in range(1, 101):
    if i ** 2 % 10 == 4:
        counter = counter + 1
print(counter)

print('\nLoop Control Statements in for loop. Break.')
# break the loop if number a number is greater than 15

numbers_2 = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in numbers_2:
    if i > 15:
        break
    print(i)

print('\nContinue Statement in for loop')

# Example: Count the total number of 'm' in a given string.

count = 0
name = 'mammals monday'

for i in name:
    if i != 'm':
        continue
    count = count + 1
print("Total 'm' count is", count)


# На вход программе подаётся натуральное число. Напишите программу, которая выводит числа от 1 до n
# включительно за исключением: чисел от 5-9 17-37 78-87

number = 90
for i in range(1, number + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i, end=' ')
print()

# На вход программе подаётся число n>1. Напишите программу, которая выводит его наименьший
# отличный от 1 делитель.

for inp in [9, 7, 10]:
    for i in range(2, inp + 1):
        if inp % i == 0:
            print('Наименьший делитель числа', inp, ':', i)
            break