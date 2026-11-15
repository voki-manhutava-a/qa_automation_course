# Основы синтаксиса Python, переменные, основные типы данных
# There are the following built-in data types in Python:
# 1. Numeric: int, float, and complex
# 2. Sequence: str, list, tuple, and range
# 3. Set: set and frozenset
# 4. Mapping: dict
# 5. Boolean: bool
# 6. Binary: bytes
# 7. None: NoneType
print('1. Python Basic Syntax, Variables, and Data Types')
print('\n2. String Data Type. Print first letter of the second word in the string')
company = 'VOKI Games'
print(type(company))
print(company)
print(company[5])  # G
print('Slice company[0:4]:', company[0:4])  # VOKI
print('Last letter company[-1]:', company[-1])  # s

print('\n3. Integer Data Type')
# int() converts a string to an integer
age = 33
player_id = int('12345')
print(type(player_id))
print('My age is:', age)
print('My player id is:', player_id)

print('\n4. Float Data Type')
weight = float('55.5') # str -> float: 55.5
height = int(170.0)  # float -> int: 170
print(type(weight))  # <class 'float'>
print('My weight is:', weight)
print('My height is:', height)

print('\n5. Complex Data Type')
complex_num = 10 + 4.5j  # real part 10.0, imaginary part 4.5
print(type(complex_num))  # <class 'complex'>
print(complex_num)  # (10+4.5j)
print(complex_num.real, complex_num.imag)  # 10.0 4.5

print('\n6. List Data Type')
fruit_salad = ['apple', 2, 'banana', 1.5]
print(type(fruit_salad))
print('Fruit salad ingredients:', fruit_salad[0], 'and', fruit_salad[2])
print('Fruit salad amount:', fruit_salad[1], 'and', fruit_salad[3])

print('\n7. Tuple Data Type')
# tuple() converts a list to a tuple
water_points_celsius = tuple([100, 0])
print(type(water_points_celsius))
print('Water Boiling Point in celsius:', water_points_celsius[0],
      'and Water Freezing Point in celsius:', water_points_celsius[1])
# water_points_celsius[1] = 5  # TypeError: 'tuple' object does not support item assignment

print('\n8. Dictionary Data Type')
cat = {
    1: 'Tom',
    2: 'Grey',
    3: 5.5
}
print(type(cat))
print('My cat name is:', cat[1], 'his color is:', cat[2], 'and his weight is:', cat[3])
print(cat)

print('\n9. Changing a Dictionary Value')
cat[3] = 6.0
print('My cat weight is now:', cat[3])

print('\n10. Heterogeneous Dictionary Elements')
dog = {
    'name': 'Rex',
    'color': 'Brown',
    'age': 5,
    'weight': 12.5,
    'is_vaccinated': True,
    'favorite_toys': ['ball', 'rope'],
}
print('My dog is:', dog['name'])
print('Color:', dog['color'])
print('Age:', dog['age'], 'years')
print('Weight:', dog['weight'], 'kg')
print('Vaccinated:', dog['is_vaccinated'])
print('Favorite toys:', dog['favorite_toys'])

print('\n11. Set Data Type')
mixed_set = {66, 'Python', 3.14, 'Version 3.9'}
print(type(mixed_set))
# The order of elements is not guaranteed, so the output of a set
# cannot be compared as a string (important for testing)
print('My set elements are:', mixed_set)

print('\n12. Adding an Element to a Set')
mixed_set.add('New Element')
print('My set elements after adding new element:', mixed_set)

print('\n13. Frozenset Data Type')
number_set = {11, 44, 75, 89, 56}
f_set = frozenset(number_set)
print(type(f_set))
print(f_set)
# f_set.add(1)  # AttributeError: 'frozenset' object has no attribute 'add'

print('\n14. Boolean Data Type')
num_a = 25
num_b = 20
is_greater = num_a > num_b
print(type(is_greater))
print('If num_a > num_b?', is_greater)
is_less = num_a < num_b
print('If num_a < num_b?', is_less)

print('\n15. NoneType')
nothing = None
print(type(nothing))
print(nothing)

print('\n16. Range Data Type')
numbers_range = range(5)
print(type(numbers_range))
print(list(numbers_range))

print('\n17. Bytes Data Type')
python_bytes = b'Python'
print(type(python_bytes))
print(python_bytes)