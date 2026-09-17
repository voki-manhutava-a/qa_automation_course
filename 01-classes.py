#Основы синтаксиса Python, переменные, основные типы данных
#there are 5 types of basic/primitive data types available in Python: 
# 1. Numeric: int, float, and complex.
# 2. Sequence: String, list, and tuple
# 3. Set 4. Dictionary (dict) and 5. Boolean (bool)
print('1. Python Basic Syntax, Variables, and Data Types')
print('\n2. String Data Type')


company = 'VOKI Games'
print(type(company))
print(company)
print(company[6])
print('\n3. Integer Data Type')
# as an integer value Using a int() class
age = 33
id = int(12345)

print(type(id))
print('My age is:', age)
print('\n4. Float Data Type')
weight = 55.5
height = float(170.75)
print(type(height))
print('My weight is:', weight)
print(height)
print('\n5. Complex Data Type')
x = 10 + 4.5j  # one int and one float
print(type(x))  # class 'complex'>
print(x)  # (9+8j)
print('\n6. List Data Type')
fruit_salad = ['apple', 2, 'banana', 1.5]
print(type(fruit_salad))
print('Fruit salad ingredients:', fruit_salad[0], 'and', fruit_salad[2])
print('Fruit salad amount:', fruit_salad[1], 'and', fruit_salad[3])
print('\n7. Tuple Data Type')
water_points_celcius = tuple((100, 0))
print(type(water_points_celcius))
print('Water Boiling Point in celcius:', water_points_celcius[0], 'and', 'Water Freezing Point in celcius:', water_points_celcius[1])
#water_points_celcius [1] = 5 #TypeError: 'tuple' object does not support item assignment
print('\n8. Dictionary Data Type')
cat = {
    1: 'Tom',
    2: 'Grey',
    3: 5.5 
}
print(type(cat))
print('My cat name is:',cat[1], 'his color is:', cat[2], 'and his weight is:', cat[3])
print (cat)
print('\n9. Changing a Dictionary Value')
cat[3] = 6.0
print('My cat weight is now:', cat[3])
print('\n10. Heterogeneous Dictionary Elements')
dog = {
    'name': 'Rex',
    'color': 'Brown',}
print('My dog name is:', dog['name'], 'and his color is', dog['color'])
print('\n11. Set Data Type')
my_set = {66, 'Python', 3.14, 'Version 3.9'}
print(type(my_set))
print('My set elements are:', my_set)   
print('\n12. Adding an Element to a Set')
my_set.add('New Element')
print('My set elements after adding new element:', my_set)  
print('\n13. Frozenset Data Type')
my_set = {11, 44, 75, 89, 56}
f_set = frozenset(my_set)
print(type(f_set))
print(f_set)
print('\n14. Boolean Data Type')
x = 25
y = 20
z = x > y
print(type(z))
print('If x > y?', z)
z = x < y
print('If x < y?', z)
