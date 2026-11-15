print('Tuples')
print('\nExercise 1: Basic Tuple Operations. Write a Python program to create a tuple, access its elements by index, and find its length.')
fruits = ("apple", "banana", "cherry", "date")
print(f'First element is {fruits[0]}. Last element: {fruits[-1]}. Tuple length is {len(fruits)}')

print('\n Exercise 2: The Trailing Comma. \nWrite a Python program to create a tuple containing a single item, the number 50, repeat a tuple three times using the *, and confirm its type.')
tuple_1 = (50,)
print(tuple_1)
print(type((50)))
print(type((50,)))
tuple_2 = tuple_1 * 3
print(f'New multiplied tuple: {tuple_2}, its type is {type(tuple_2)}')


print('\nExercise 3: Tuple Concatenation and slicing')
print('3.1  Write a Python program to join three separate tuples into one new tuple using the + operator.')
a = (1, 2) 
b = (3, 4)
c = (5, 6)
d = a + b + c
print(d)
print('3.2 Write a Python program to extract a specific portion of a tuple using slice notation.')
print('Sliced tuple:', d[2:5])
print('Reversed tuple:', d[::-1])
print('Every second element:', d[::2])

print('\nExercise 4. Tuple Filtering. Write a Python program to filter a tuple and keep only the elements that satisfy a given condition (values greater than 10), using both filter() and a list comprehension approach.')
numbers = (3, 14, 7, 22, 9, 41, 18, 5)
filtered_by_lambda = tuple(filter(lambda x: x > 10, numbers))
print(filtered_by_lambda)
filtered_by_comprehension = tuple([x for x in numbers if x > 10])
print(filtered_by_comprehension)

print('\nImmutability of a tuple')
# fruits[0] = "orange"  # TypeError: 'tuple' object does not support item assignment

print('\nTuple unpacking')
x, y = (10, 20)
print(x, y)
first, *rest = (1, 2, 3, 4)
print(first, rest)

print('\nTuple methods')
print(numbers.count(7))
print(numbers.index(22))