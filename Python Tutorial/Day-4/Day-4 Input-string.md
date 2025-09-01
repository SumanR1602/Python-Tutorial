# Day-4 Taking Input from the User in Python

In Python, you can take input from the user using the `input()` function.  
By default, the value returned by `input()` is always a string.

**Syntax:**
```python
variable = input("Prompt message: ")
```

**Example:**
```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

### Type Casting User Input

Since `input()` always returns a string, you often need to convert (type cast) the input to another data type for calculations.

**Example:**
```python
age = input("Enter your age: ")   # age is a string
print(age, type(age))             # Output: e.g. 21 <class 'str'>

age = int(age)                    # Convert to integer
print(age, type(age))             # Output: 21 <class 'int'>
```

Or, you can combine input and type casting in one line:

```python
marks = float(input("Enter your marks: "))  # Directly converts input to float
print(marks, type(marks))
```

