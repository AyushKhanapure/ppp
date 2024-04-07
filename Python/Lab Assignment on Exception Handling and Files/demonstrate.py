# 1. SyntaxError
print("Demonstrating SyntaxError:")
# SyntaxError: missing parentheses in print statement
# print "Hello, World!"

# 2. TypeError
print("\nDemonstrating TypeError:")
# TypeError: concatenation of 'int' and 'str' objects
# result = 5 + "Hello"

# 3. IndexError
print("\nDemonstrating IndexError:")
# IndexError: list index out of range
# my_list = [1, 2, 3]
# print(my_list[3])

# 4. ValueError
print("\nDemonstrating ValueError:")
# ValueError: invalid literal for int() with base 10: 'abc'
# number = int("abc")

# 5. ZeroDivisionError
print("\nDemonstrating ZeroDivisionError:")
# ZeroDivisionError: division by zero
# result = 5 / 0

# 6. FileNotFoundError
print("\nDemonstrating FileNotFoundError:")
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
# with open("nonexistent.txt", "r") as file:
#     contents = file.read()
