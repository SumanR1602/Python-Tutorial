# Day 4 - Type Casting & Input in Python: Theory

##  Theoretical Questions

1. What is type casting in Python? Why is it important?
2. What is the difference between implicit and explicit type casting? Give examples.
3. What will be the data type of the value returned by the `input()` function? Why?
4. Why do we often need to use type casting with user input?
5. List at least three built-in functions used for type casting in Python and explain what they do.
6. What will happen if you try to convert a non-numeric string to an integer using `int()`?
7. Explain the difference between `str(123)` and `int("123")`.
8. Can you convert a list to a tuple? How?
9. What is the output type of the following operation: `int(3.99)`?
10. What is the difference between `int("10")` and `float("10")`?

---

## Problem-Solving Questions

1. What will be the output?  
    ```python
    x = "5"
    y = 2
    print(x * y)
    ```
2. What will happen if you run this code?  
    ```python
    a = "abc"
    b = int(a)
    print(b)
    ```
3. What is the output and type of `input("Enter a number: ") + 5` if the user enters `10`?
4. What will be printed?  
    ```python
    x = float("5") + int("2")
    print(x, type(x))
    ```
5. What is the output?  
    ```python
    s = "123.45"
    print(int(float(s)))
    ```
6. What will happen if you run this code?  
    ```python
    l = [1, 2, 3]
    print(tuple(l))
    print(str(l))
    ```
7. What is the output?  
    ```python
    print(list("abc"))
    ```
8. What will be printed?  
    ```python
    print(int(True), float(False))
    ```
9. What will happen if you run this code?  
    ```python
    print(int("10.5"))
    ```
10. What is the output?  
    ```python
    print(type(input("Enter anything: ")))
    ```

---
