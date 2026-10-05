import os
import shutil
import random
import numpy as np


print('Exercise 1\nWrite a Python program that prints the current working directory to the console.')


print("Current Directory:", os.getcwd())

print('Exercise 2. List Directory Contents\nWrite a Python program that lists all files and folders in a given directory path.')

path = os.listdir()
for i in path:
    print(i)
# print(os.listdir())

print('Exercise 3: Create a Directory\nWrite a Python program that creates a new folder called test_folder in the current working directory, only if it does not already exist.')

os.makedirs("new_folder", exist_ok=True)

if not os.path.exists('new_folder'):
    os.mkdir('new_folder')
    print(f"Folder '{'new_folder'}' created successfully.")
else:
    print(f"Folder '{'new_folder'}' already exists.")
    
print('Exercise 5: Rename a File. Write a Python program that renames a file called old.txt to new.txt in the current directory, with a check to confirm the source file exists before attempting the rename.')
open("old.txt", "w").close()

if os.path.exists('old.txt'):
    print('File exists')
    os.rename("old.txt", "new.txt")
    print('File has been renamed')
else:
    print('file does not exist')
    
print('Exercise 6: Delete a File\nWrite a Python program that deletes a file called temp.txt from the current directory, but only after verifying that the file actually exists.')
open("temp.txt", "w").close()

if os.path.exists('temp.txt'):
    print('File exists')
    os.remove('temp.txt')
    print('File has been removed')
else:
    print('file does not exist')
    
print('Exercise 7: Delete a Directory Tree\nWrite a Python program that creates a nested directory structure cleanup/a/b, adds a dummy file inside it, then removes the entire tree including all contents.')

os.makedirs('cleanup/a/b', exist_ok=True)
open('cleanup/a/b/dummy.txt', 'w').close()

if os.path.exists('cleanup'):
    shutil.rmtree('cleanup')
    print(f"Directory has been removed entirely including all contents.")
    
else:
    print(f"Folder does not exist.")
    
print('Exercise 8: Set an Environment Variable')
os.environ['MY_VARIABLE'] = "hello"
value = os.environ.get("MY_VARIABLE", "not set")
print(f'Enviroment virable set as: {value}')
    
    
print('Exercise 8: Generate 3 Random Integers\nWrite a code to generate 3 random integers between 100 and 999 which is divisible by 5')


for i in range (3):
    print(random.randrange(100, 999, 5))
    

print('Exercise 9: Random Lottery Pick\nWrite a code to generate 100 random lottery tickets and pick two lucky tickets from it as a winner. Note you must adhere to the following conditions. The lottery number must be 10 digits long. All 100 ticket number must be unique.')

tickets = random.sample(range(1000000000, 9999999999), 100)
winners = []

for i in range(2):
    winners.append(tickets[random.randint(0, len(tickets))])
print(winners)

print('Exercise 10. Create a 1D NumPy array of numbers from 0 to 9')

arr = np.array(range(10))
print(arr)

print('Exercise 11: Convert 1D array to 2D\nWrite a code to convert a 1D array to a 2D array with 2 rows.')
arr = np.arange(6)
newarr = arr.reshape(2, 3)
print(newarr)

print('Exercise 12: Create a 4x4 array and extract its first row and last column')

arr2 = np.arange(1, 17).reshape(4, 4)
print(arr2)
row = arr2[0]
clm = arr2[:, -1]
print("First Row:", row)
print("Last Column:", clm)

    
