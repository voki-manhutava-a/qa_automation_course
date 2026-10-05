print('Dictionaries')
print('Get all keys and values')
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(person.keys())
print(person.values())
print(person.items())
print('Iterating a dictionary')
for i in person:
    print(i, ':', person[i])
    
    
print('Iterating using items')
for key_value in person.items():
    print(key_value[0], key_value[1])
print('Another option to iterate:')
for key, value in person.items():
    print(key, ':', value)
    
print('\nExercise 1')
print('Write a Python program to add a new key-value pair to a dictionary, modify an existing value, access a specific key, and check whether a given key exists')
student = {"name": "Alice", "age": 20, "grade": "B"}

print('Adding a new utem using update method:')
student.update({"city": "New York"})

print(student)
print('Adding a new utem using key-value assignment:')

student['class'] = 'Chemistry'
print(student)

print('Modify a value using update and access a specific key')
student.update({'name': 'Ann'})
print("Name:", student["name"])
print('Check whether a given key exists')
search = 'grade'

if search in student:
    print('Studen`t grade is', student[search])
else: 
    print('Value is not found')
    
print('\n Exercise 2')
print(': Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.')
text = "hello world"
new_dict = {}
for i in text:
    new_dict[i] = new_dict.get(i, 0) + 1
print(new_dict)

print('\n Exercise 3. Filter Dictionary')
print('Write a Python program to create a new dictionary containing only the key-value pairs from an existing dictionary where the value meets a specified condition - keep only scores greater than 60')
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
new = {}

for k, v in scores.items():
    if v > 60:
        new[k] = v
print(new)