'''This function adds two numbers
and returns the result.'''
def add(a,b):
    return a+b

'''This function subtracts two numbers
and returns the result.'''
def subtract(a,b):
    return a-b

'''This function multiplies two numbers
and returns the result.'''
def multiply(a,b):
    return a*b

'''This function divides two numbers
and returns the result.'''
def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Division by zero error"


print(add(2,3))
print(subtract(5,2))
print(multiply(3,4))
print(divide(10,2))