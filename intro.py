num = 3
print(type(num)) # => <class 'int'>

num = 3.14
print(type(num)) # => <class 'float'>

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Float Division:   3 // 2 (Drops decimals)
# Exponent:         3 ** 2
# Modulus:          3 % 2

print(3 / 2) # => 1.5
print(3 // 2) # => 1
print(3 ** 2) # => 9


num = 1
num += 10
print(num) # => 11

print(abs(-3)) # => 3

print(round(3.75)) # => 4
print(round(3.75, 1)) # => 3.8

# Comparisons:
# Equal:                3 == 2
# Not Equal:            3 != 2
# Greater Than:         3 > 2
# Less Than:            3 < 2
# Greater or Equal:     3 >= 2
# Lesser or Equal:      3 <= 2

print(3 != 2) # => True

num_1 = '100'
num_2 = '200'
print(num_1 + num_2) # => 100200

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2) # => 300
