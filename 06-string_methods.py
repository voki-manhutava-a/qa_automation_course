print('Exercise 1. Split method')
print('Split string into a list')
string = 'Prints the values to a stream, or to sys`stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys`stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline. flush: whether to forcibly flush the stream.'
sentences = string.split('.')
k = 0
for i in sentences:
    print(sentences[k], '\n')
    k += 1
    
print('\nExercise 2. strip() method. \n Remove Whitespace')
str1 = " Python    "
print(str1.strip())
print('It can remove specified characters:', "---Hello---".strip("-"))

print('\nExercise 3. strip() method. \n Remove Whitespace')
str2 = " P y t h o n "
res = str2.replace(" ", "")
print("Cleaned string:", res)

print('\nExercise 4. String Partitioning. \n Use the .partition() method to split a string into three parts: the part before a separator, the separator itself, and the part after it.')
str3 = "username@company.com" #sep = "@"
res2 = str3.partition('@')
print(f'Partitioned Result: {res2[0]}')

print('\n Exercise 5. In operator. \n Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character`s position doesn`t matter.')

s1 = "yN"
s2 = "Pynative"

flag = bool()
for char in s1:
    if char.lower() in s2.lower():
        flag = True
    else:
        flag = False
        break

print("Is s1 and s2 balanced:", flag)


