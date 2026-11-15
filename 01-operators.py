print("1. Python Arithmetic Operators")
num_a = 17
num_b = 5

print("\n2. Addition '+'")
print("Addition of num_a and num_b is:", num_a + num_b)  # 22

print("\n3. Subtraction '-'")
print("Subtraction of num_a and num_b is:", num_a - num_b)  # 12

print("\n4. Multiplication '*'")
print("Multiplication of num_a and num_b is:", num_a * num_b)  # 85

print("\n5. Division '/'")
# The '/' operator always returns a float (exact division)
print("Division of num_a and num_b is:", num_a / num_b)  # 3.4

print("\n6. Modulus '%'")
# The remainder after division: 17 = 5 * 3 + 2
print("Modulus of num_a and num_b is:", num_a % num_b)  # 2

print("\n7. Exponentiation '**'")
base = 2
exponent = 8
print("Exponentiation of base and exponent is:", base ** exponent)  # 256

print("\n8. Floor Division '//'")
# The whole part of the division, the fractional part is dropped
print("Floor Division of num_a and num_b is:", num_a // num_b)  # 3

print("\n9. Python Assignment Operators")
number = 5
print("Initial value of number is:", number)

print("\n10. Addition Assignment Operator")
number += 3
print("Value of number after number += 3 is:", number)  # 8

print("\n11. Subtraction Assignment Operator")
number -= 2
print("Value of number after number -= 2 is:", number)  # 6

print("\n12. Multiplication Assignment Operator")
number *= 4
print("Value of number after number *= 4 is:", number)  # 24

print("\n13. Division Assignment Operator")
# '/' always returns a float, even if the division is exact:
# the result is 12.0, not 12, and str(number) gives '12.0'
number /= 2
print("Value of number after number /= 2 is:", number)  # 12.0
print("Type of number is now:", type(number))  # <class 'float'>

print("\n14. Modulus Assignment Operator")
# number is a float after section 13 (12.0 % 3 would give 0.0),
# so we set an int value again
number = 10
number %= 3  # remainder of division
print("Value of number after number %= 3 is:", number)  # 1

print("\n15. Floor Division Assignment Operator")
number = 10
number //= 3
print("Value of number after number //= 3 is:", number)  # 3

print("\n16. Exponentiation Assignment Operator")
number = 5
number **= 3  # power
print("Value of number after number **= 3 is:", number)  # 125

print("\n17. Bitwise AND Assignment Operator")
# '&' gives 1 only if BOTH bits are 1
bits_a = 12  # 1100
bits_b = 10  # 1010
bits_a &= bits_b
print("Value of bits_a after bits_a &= bits_b is:", bits_a)  # 8 (1000)

print("\n18. Bitwise OR Assignment Operator")
# '|' gives 1 if AT LEAST ONE bit is 1
bits_a = 12  # 1100
bits_b = 10  # 1010
bits_a |= bits_b
print("Value of bits_a after bits_a |= bits_b is:", bits_a)  # 14 (1110)

print("\n19. Bitwise XOR Assignment Operator")
# '^' gives 1 only if the bits are DIFFERENT
bits_a = 12  # 1100
bits_b = 10  # 1010
bits_a ^= bits_b
print("Value of bits_a after bits_a ^= bits_b is:", bits_a)  # 6 (0110)

print("\n20. Right Shift Assignment Operator")
# Shifting right by n bits is the same as floor division by 2 ** n
number = 150  # 10010110
number >>= 2  # 150 // 4
print("Value of number after number >>= 2 is:", number)  # 37 (100101)

print("\n21. Left Shift Assignment Operator")
# Shifting left by n bits is the same as multiplication by 2 ** n
number = 17  # 10001
number <<= 3  # 17 * 8
print("Value of number after number <<= 3 is:", number)  # 136 (10001000)

print("\n22. Python Comparison Operators")
first_num = 10
second_num = 14

print("\n23. Equal to '=='")
print("Is first_num equal to second_num? -", first_num == second_num)  # False

print("\n24. Not equal to '!='")
print("Is first_num not equal to second_num? -", first_num != second_num)  # True

print("\n25. Greater than '>'")
print("Is first_num greater than second_num? -", first_num > second_num)  # False

print("\n26. Less than '<'")
print("Is first_num less than second_num? -", first_num < second_num)  # True

print("\n27. Greater than or equal to '>='")
print("Is first_num greater than or equal to second_num? -", first_num >= second_num)  # False

print("\n28. Less than or equal to '<='")
print("Is first_num less than or equal to second_num? -", first_num <= second_num)  # True

print("\n29. Chain comparison operators")
value = 5
print("Is 1 < value < 10?", 1 < value < 10)  # True
print("Is 1 < value and value < 10?", 1 < value and value < 10)  # True

print("\n30. Logical Operators")
value = 15
print("'and' is True only if both statements are true")
print("value < 5 and value < 10:", value < 5 and value < 10)  # False
print("value > 10 and value < 20:", value > 10 and value < 20)  # True
print("'or' is True if at least one statement is true")
print("value < 20 or value < 10:", value < 20 or value < 10)  # True
print("value < 5 or value > 20:", value < 5 or value > 20)  # False
print("'not' reverses the result")
print("not (value < 5 and value < 10):", not (value < 5 and value < 10))  # True

print("\n31. Short-circuit evaluation")
# In 'a and b' with a false 'a', 'b' is not evaluated at all,
# so 1 / 0 does not raise ZeroDivisionError
print("value < 5 and 1 / 0 > 0:", value < 5 and 1 / 0 > 0)  # False
# In 'a or b' with a true 'a', 'b' is not evaluated either
print("value < 20 or 1 / 0 > 0:", value < 20 or 1 / 0 > 0)  # True