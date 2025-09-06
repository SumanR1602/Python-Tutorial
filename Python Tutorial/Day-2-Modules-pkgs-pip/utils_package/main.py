'''Modules and Packages Implimentation'''
import math_utils
print(math_utils.add(5, 10)) # This will print the sum of 5 and 10
print(math_utils.subtract(10, 5)) # This will print the difference of 10 and 5

'''Comments and Escape characters,their usage'''
print(math_utils.multiply(5, 10),math_utils.divide(10, 5),sep=',')
# This will cause an error:
# print("This doesn't "execute""')

# Correct usage with escape sequence:
print("This will \"execute\"")


'''Variables and Data Types Implementation'''
# Numeric
age = 25          # int
pi = 3.14         # float
c = 2 + 3j        # complex

# Text
name = "Alice"    # str

# Collection
numbers = [1, 2, 3]       # list (mutable)
colors = ("red", "blue")   # tuple (immutable)
unique_numbers = {1, 2, 3} # set (mutable)
data = {"a": 1, "b": 2}    # dict (mutable)

# Boolean
is_adult = True            # bool

# Checking types
print(type(age))           # <class 'int'>
print(type(colors))        # <class 'tuple'>

