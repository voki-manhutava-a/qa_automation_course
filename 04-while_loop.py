#На вход программе подаётся натуральное число. Напишите программу, которая выводит числа от 1 до n
# включительно за исключением: чисел от 5-15 17-37 78-87

print('1. Python while loop')

print('\n1.1 Run loop till count is less than 3')

count = 1
while count < 3:
    print(count)
    count = count + 1
    
print('\n1.2 Check how many times a given number can be divided by 3 before it is less than or equal to 10')

number = 100
count = 0

while number > 10:
    number = number / 3
    count += 1
print('Total iteration required:', count)

print('\n1.3 Ask the user to enter a number between 100 and 500. We will keep asking the user to enter a correct input until he/she enters the number within a given range. The code below has to be uncommented and run in terminal, because it requires input.')

#number = int(input('Enter any number between 100 and 500 '))
#while number < 100 or number > 500:
#    print('Incorrect number, Please enter correct number:')
#    number = int(input('Enter a Number between 100 and 500 '))
#else:
#    print("Given Number is correct", number)

print('\n2 If-else in while loop')
print('2.1Print even and odd numbers between 1 to the entered number.')
num = 15
while num > 0:
    if num % 2 == 0:
        print(num, 'It`s and even number ')
    else:
        print(num, 'It`s an odd number')
    num = num - 1
    
print('\n3 Break in while loop')

print('3.1 Write a while loop to display each character from a string and if a character is a number, then stop the loop.')
        
name = 'Jesaa29Roy'
size = len(name)
i = 0
while i < size:
    if name[i].isdecimal():
        break;
    print(name[i], end=' ')
    i = i + 1
        
print('\n 4. Continue statement')
print('\n 4.1 Write a while loop to display only alphabets from a string.')


name = 'Jesaa29Roy'
size = len(name)
i = -1
while i < size - 1:
   i = i + 1
   if not name[i].isalpha():
       continue
   print(name[i], end=' ')
    


print('\n 5. Nested while loops')
print('\n 5.1 Use nested while loop to print a pattern')

asteriks = '*'
i = 0
while i < 5:
    j = 0
    while j < i:
        print(asteriks, end=' ')
        j = j + 1
    print(' ')
    i = i + 1
    
#В задании был такой пример кода, хотя у меня получилось сделать без вложенного цикла
# i = 0
# while i < 5:
#     print('* ' * i)
#     i+=1


print('5.2 Цифровым корнем числа n называется число, получающееся следующим образом: вычисляется сумма цифр числа n затем сумма цифр у получившегося числа и так далее, пока не получится однозначное число.  Например, цифровой корень числа 9875 равен 2. Напишите программу, которая находит цифровой корень данного числа')

number = 1208
inputnumber = 1208
while number >= 10:
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    number = sum
print('\n Цифровой коренть числа', inputnumber, 'равен', number)
