print('Lists')
print('Exercise 1. Perform Basic List Operations')
numbers = [10, 20, 30, 40, 50]
print('Write a script to perform the following three operations on given list.')

# Access the third element of a list
# List Length: Print the total number of items
# Check if the list is empty
print('\nAccess the third element of a list ')
print(f'Third element of the list is {numbers[2]}')
print('\n List Length: Print the total number of items')
print(f'Length of the list is {len(numbers)}')
print('\n Check if the list is empty')
is_empty = len(numbers) == 0
print(f'If the list is empty? {is_empty}')
empty_list = []
# an empty list is False in a condition, so "not empty_list" is the usual way to check it
print(f'If the empty list is empty? {not empty_list}')

print('\nExercise 2. Perform List Manipulation')

# Practice Problem: Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 to the end of a list and print the new list.
# Insert Element: Insert 300 at the third position of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.
# Exercise Purpose: Python lists are mutable, meaning they can be changed after
# they are created. This exercise demonstrates the various ways to “reshape” your data dynamically during execution.

list_01 = [100, 50, 400, 500]

print('Change Element: Change the second element of a list to 200 and print the updated list.')
list_01[1] = 200
print(list_01)
print('\nAppend Element: Add 600 to the end of a list and print the new list.')
list_01.append(600)
print(list_01)
print('\nInsert Element: Insert 300 at the third position of a list and print the result.')
list_01.insert(2, 300)
print(list_01)
print('\nRemove Element (by value): Remove 600 from the list and print the list.')
# remove() raises ValueError if the value is not in the list
list_01.remove(600)
print(list_01)
print('\nRemove Element (by index): Remove the element at index 0 from the list')
# pop() returns the removed element
removed = list_01.pop(0)
print('Removed element:', removed)
print(list_01)


print('\nExercise 3. Loop Through a List')
print('Iterate along with an index number')

my_list = [5, 8, 'Tom', 7.50, 'Emma']

for i in range(len(my_list)):
    print(i, my_list[i])

print('Count Even and Odd Numbers')

# Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

integers = [10, 21, 4, 45, 66, 93, 11]
odd = 0
even = 0

for i in integers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Amount of odd numbers is {odd}, amount of even numbers is {even}')

print('\nExercise 4. Find an object using while')

print('Дан список чисел. Найди индекс первого отрицательного числа в списке, используя цикл while (без for и без встроенных функций типа index).')

# first, middle, last position, no negative numbers, empty list
lists_to_check = [[-5, 2, 3], [4, 8, 15, -3, 16, -7, 23], [1, 2, -9], [1, 2, 3], []]
for numbers_with_negatives in lists_to_check:
    i = 0
    while i < len(numbers_with_negatives):
        if numbers_with_negatives[i] < 0:
            print(numbers_with_negatives, '- индекс первого отрицательного числа:', i)
            break
        i += 1
    else:
        # else runs only if the loop finished without break
        print(numbers_with_negatives, '- отрицательных чисел нет')