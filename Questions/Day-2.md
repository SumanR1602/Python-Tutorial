#  Day 2 - Q/A: Comments, Escape Sequences, Modules & Packages

##  Theory Questions

### 1. Comments & Escape Sequences

- **Q1:** What is the difference between a single-line comment and a multi-line comment in Python? Give examples.
- **Q2:** Why are comments important in programming?
- **Q3:** What is an escape sequence? Name at least three escape sequences and explain their use.
- **Q4:** What will the following code output?  
  ```python
  print("Hello\tWorld\nPython")
  ```
- **Q5:** How do you print a file path like `C:\Users\Student\Documents` in Python without causing an error?

---

### 2. Modules & Packages

- **Q6:** What is a module in Python? How is it different from a package?
- **Q7:** Why do we use modules and packages in Python projects?
- **Q8:** What is the purpose of the `__init__.py` file inside a package?
- **Q9:** How do you import a function named `add` from a module called `math_utils` inside a package called `utils_package`?
- **Q10:** What is the difference between a built-in module and an external (third-party) module? Give examples.

---

##  Conceptual & Trick Questions

### 3. Comments & Escape Sequences

- **Q11:** Will the following code run without errors? Why or why not?
  ```python
  print('It\'s a sunny day')
  print("He said, "Hello!"")
  ```
- **Q12:** What will be the output of this code?
  ```python
  print("A\\B\\C")
  ```
- **Q13:** How would you print the following exactly as shown (including the quotes)?
  ```
  "Python's power"
  ```

---

### 4. Modules & Packages 

- **Q14:** Suppose you have a file `math_utils.py` with a function `add(a, b)`. You import it using:
  ```python
  import math_utils
  print(add(2, 3))
  ```
  Will this work? Why or why not?

- **Q15:** If you have the following structure:
  ```
  utils_package/
      __init__.py
      math_utils.py
  ```
  And in `main.py` you write:
  ```python
  from utils_package import math_utils
  print(math_utils.add(2, 3))
  ```
  What must be true for this code to work? (Consider file locations and Python path.)

- **Q16:** What happens if you remove the `__init__.py` file from the `utils_package` folder? Can you still import `math_utils` as a package module?

- **Q17:** If you write `import math_utils` in `main.py` but get a `ModuleNotFoundError`, what could be the possible reasons?

- **Q18:** What is the output of the following code?  
  ```python
  print("Hello", "World", sep='***', end='!!!')
  ```
- **Q19:** What is the difference between `import math_utils` and `from math_utils import add`?

---

## Coding Problems

### 5. Practice Problems

- **Q20:** Write a function in `math_utils.py` called `multiply(a, b)` and show how to import and use it in `main.py`.

- **Q21:** Given the following code, what will be the output?  
  ```python
  print("Line1\nLine2\tTabbed\\Backslash")
  ```

- **Q22:** What will happen if you try to import a module that does not exist? Write the code and explain the error.

- **Q23:** Suppose you have the following in `math_utils.py`:
  ```python
  def add(a, b):
      return a + b

  def add(a, b, c):
      return a + b + c
  ```
  What will happen if you call `add(2, 3)` from another file? Why?

- **Q24:** In `main.py`, you write:
  ```python
  from utils_package.math_utils import add
  print(add(2, 3))
  ```
  But you get an error. List at least two possible reasons for this error.


##  Variables & Data Types  Questions

1. **Q1:** What will be the type and value of `x` after these statements?
    ```python
    x = 5
    x = "5"
    ```
2. **Q2:** Is the following variable name valid? Why or why not?
    ```python
    1st_value = 10
    ```
3. **Q3:** What is the difference between a mutable and an immutable data type? Give one example of each.

4. **Q4:** What will be the output and type of the following?
    ```python
    a = [1, 2, 3]
    b = a
    b[0] = 100
    print(a)
    ```
5. **Q5:** What is the output of the following code? Explain why.
    ```python
    x = None
    print(type(x))
    ```
6. **Q6:** What is the difference between `list`, `tuple`, and `set` in terms of mutability and syntax?
7. **Q7:** What will happen if you try to assign a value to a string index, like this?
    ```python
    name = "Alice"
    name[0] = "a"
    ```
8. **Q8:** What is dynamic typing in Python? Give an example.

---

## Operators in Python

1. **Q1:** What will be the output?
    ```python
    print(2 + 3 * 4)
    print((2 + 3) * 4)
    ```

2. **Q2:** What is the result of:
    ```python
    x = 5
    x += 3 * 2
    print(x)
    ```

3. **Q3:** What will be printed?
    ```python
    print(True + True * False)
    ```

4. **Q4:** What is the output?
    ```python
    print(5 & 3)
    print(5 | 3)
    print(5 ^ 3)
    ```

5. **Q5:** What will be the output?
    ```python
    a = [1, 2, 3]
    b = a
    print(a is b)
    print(a == b)
    ```

6. **Q6:** What is the output?
    ```python
    print(10 > 5 > 2)
    print(10 > 5 < 2)
    ```

7. **Q7:** What will be printed?
    ```python
    x = 4
    x //= 2
    x **= 3
    print(x)
    ```

8. **Q8:** What is the output?
    ```python
    print(2 ** 3 ** 2)
    ```

9. **Q9:** What will be the output?
    ```python
    print(3 in [1, 2, 3])
    print(4 not in [1, 2, 3])
    ```

10. **Q10:** What is the output?
    ```python
    a = 256
    b = 256
    print(a is b)
    c = 257
    d = 257
    print(c is d)
    ```