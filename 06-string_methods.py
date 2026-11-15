print('Exercise 1. Split method')
print('Split string into a list')
string = "Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline. flush: whether to forcibly flush the stream."
sentences = string.split('.')
for sentence in sentences:
    print(sentence, '\n')
    
print('\nExercise 2. strip() method. \n Remove Whitespace')
padded_text = " Python    "
print(padded_text.strip())
print('It can remove specified characters:', "---Hello---".strip("-"))

print('\nExercise 3. replace() method. \n Remove Whitespace')
spaced_text = " P y t h o n "
# strip() removes spaces only at the edges, replace(" ", "") removes them everywhere
cleaned = spaced_text.replace(" ", "")
print("Cleaned string:", cleaned)

print('\nExercise 4. String Partitioning. \n Use the .partition() method to split a string into three parts: the part before a separator, the separator itself, and the part after it.')
email = "username@company.com" #sep = "@"
parts = email.partition('@')
print(f'Partitioned Result: {parts}')

print("\n Exercise 5. In operator. \n Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character's position doesn't matter.")

s1 = "yN"
s2 = "Pynative"
s2_lower = s2.lower()

flag = True
for char in s1.lower():
    if char not in s2_lower:
        flag = False
        break

print("Is s1 and s2 balanced:", flag)