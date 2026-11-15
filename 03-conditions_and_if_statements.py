print("1. Python Conditions and If statements")

print("\n1.1 If statement")
positive_number = 15
if positive_number > 0:
    print("The number is positive")

print("\n1.2 Boolean variables can be used directly in if statements without comparison operators")
is_logged_in = True
if is_logged_in:
    print("Welcome back!")

print("\n2. elif statement")
# The elif keyword allows you to check multiple expressions for True
# and execute a block of code as soon as one of the conditions evaluates to True.
# Each value tests a different branch: three elif/if branches and else
for menu_timing in ["Breakfast", "Lunch", "Dinner", "Brunch"]:
    if menu_timing == "Breakfast":
        print(menu_timing, "- Enjoy your breakfast!")
    elif menu_timing == "Lunch":
        print(menu_timing, "- Enjoy your meal!")
    elif menu_timing == "Dinner":
        print(menu_timing, "- Bon appétit!")
    else:
        print(menu_timing, "- Wrong entry")

print("\n3. else statement")
# password = input("Enter password! ")  # user input, commented out so the code runs on its own
# Both branches: the correct and the incorrect password
for password in ["123", "456"]:
    if password == "123":
        print(password, "- Correct password")
    else:
        print(password, "- Incorrect password")

print("\n4. Nested if-else statement")

print("\n4.1 Find a greater number between two numbers")
# All three branches: first is greater, first is smaller, numbers are equal
for first_num, second_num in [(54, 33), (33, 54), (40, 40)]:
    if first_num >= second_num:
        if first_num == second_num:
            print(first_num, "and", second_num, "are equal")
        else:
            print(first_num, "is greater than", second_num)
    else:
        print(first_num, "is smaller than", second_num)

print("\n4.2 Checking even or odd numbers")
for even_odd_number in [7, 10]:
    if even_odd_number % 2 == 0:
        print(even_odd_number, "- the number is even")
    else:
        print(even_odd_number, "- the number is odd")

print("\n5. Task: access for students who are at least 12 years old and in at least 7th grade")
# All four combinations of the two conditions joined by 'and'
for age, grade in [(13, 8), (11, 8), (13, 6), (11, 6)]:
    if age >= 12 and grade >= 7:
        print("Age:", age, "Grade:", grade, "- access granted.")
    else:
        print("Age:", age, "Grade:", grade, "- access denied.")

print("\n6. Task: determine whether a natural number is three-digit")
# Boundary values: 99, 100, 999, 1000; also 0 and a negative number
for three_digit_number in [99, 100, 999, 1000, 0, -999]:
    if 100 <= three_digit_number <= 999:
        print(three_digit_number, "is a three-digit number.")
    elif three_digit_number <= 0:
        # natural numbers start from 1, so 0 is not natural either
        print(three_digit_number, "is not a natural number.")
    else:
        print(three_digit_number, "is not a three-digit number.")

print("\n7. Task: check that all three digits of a three-digit natural number are different")
# 123 - all different, 121 and 111 - repeated digits, 99 and 1221 - not three-digit
for digits_number in [123, 121, 111, 99, 1221]:
    if 100 <= digits_number <= 999:
        hundreds = digits_number // 100        # 123 // 100 = 1 (drop the last two digits)
        tens = digits_number // 10 % 10        # 123 // 10 = 12, then 12 % 10 = 2
        units = digits_number % 10             # 123 % 10 = 3 (the last digit)
        if hundreds != tens and hundreds != units and tens != units:
            print(digits_number, "has all different digits.")
        else:
            print(digits_number, "does not have all different digits.")
    else:
        print(digits_number, "is not a three-digit number.")

