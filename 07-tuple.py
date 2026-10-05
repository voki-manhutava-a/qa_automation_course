print('Tuples')
print('\nExercise 1: Basic Tuple Operations. Write a Python program to create a tuple, access its elements by index, and find its length.')
fruits = ("apple", "banana", "cherry", "date")
print(f'First element is {fruits[0]}. Last element: {fruits[-1]}. Tuple lenghth is {len(fruits)}')

print('\n Exercise 2: The Trailing Comma. \nWrite a Python program to create a tuple containing a single item, the number 50, repeat a tuple three times using the *, and confirm its type.')
tuple_1 = (50,)
print(tuple_1)
tuple_2 = tuple_1 * 3
print(f'New multiplied tuple: {tuple_2}, its type is {type(tuple_2)}')


print('Exercise 3: Tuple Concatenation and slicing')
print('3.1  Write a Python program to join three separate tuples into one new tuple using the + operator.')
a = (1, 2) 
b = (3, 4)
c = (5, 6)
d = a + b + c
print(d)
print('3.2 Write a Python program to extract a specific portion of a tuple using slice notation.')
print('Sliced tuple:', d[2:5])

print('Exercise 4. Tuple Filtering. Write a Python program to filter a tuple and keep only the elements that satisfy a given condition (values greater than 10), using both filter() and a list comprehension approach.')
numbers = (3, 14, 7, 22, 9, 41, 18, 5)
result = tuple(filter(lambda x: x > 10, numbers))
print(result)
result_2 = list([])
for i in numbers:
    if i > 10:
        result_2.append(i)
result_2 = tuple(result_2) 
print(result_2)