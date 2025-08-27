# Problem-Solving Questions

## 1️. Modules & Packages 

1. If you have a file named `tools.py` with:
    ```python
    def add(x, y): 
        return x + y
    def sub(x, y): 
        return x - y
    ```
    and in `main.py` you write:
    ```python
    import tools
    print(tools.add(2, 3))
    print(tools.sub(5, 2))
    ```
    What will be the output?

2. What happens if you try to import a module that does not exist? Write the code and the error message.

3. If you have a folder named `myutils` with a file `maths.py` inside it, and you want to use a function `square(x)` from `maths.py` in your `main.py`, how would you import and use it?

4. What will be printed?
    ```python
    # file: config.py
    setting = "A"

    # file: main.py
    import config
    config.setting = "B"
    print(config.setting)
    ```

5. What happens if you import the same module twice in a script? Will its code run twice?


6. If you have two files, `alpha.py` and `beta.py`, both in the same folder, and both define a function called `show()`, what happens if you do `import alpha` and `import beta` in your main file? How do you call each `show()`?

---

## 2️. Comments & Escape Characters

1. What will be printed?
    ```python
    print("First line\\nSecond line")
    print("First line\nSecond line")
    ```

2. What is the output?
    ```python
    print("Tab\\tSpace")
    print("Tab\tSpace")
    ```

3. Will this code run? Why or why not?
    ```python
    # print("Hello)
    print("World")
    ```

4. What will be printed?
    ```python
    print("She said, \"It's Python!\"")
    print('He replied, "Yes, it\'s fun!"')
    ```

5. What is the output?
    ```python
    print("Backslash: \\\\")
    ```

6. What will be printed?
    ```python
    print("Hello", end="\\n")
    print("World", end="\n")
    ```

7. What will be printed?
    ```python
    print("Line1\nLine2\tTabbed\\Backslash")
    ```

8. What is the output?
    ```python
    print("He said, \"Hello!\"\nShe replied, 'Hi!'\n")
    print('''This is a
    multi-line
    string''')
    ```

9. Will this code run? Why or why not?
    ```python
    '''
    print("This is a comment")
    '''
    print("Done")
    ```

---

## 3️. Variables, Data Types & Operators

1. What will be printed?
    ```python
    print(type(3.0))
    print(type([1, 2, 3]))
    print(type((1, 2, 3)))
    print(type({1, 2, 3}))
    ```

2. What is the output?
    ```python
    x = 10
    x = x / 2
    print(type(x))
    ```

3. What will be printed?
    ```python
    my_set = {1, 2, 2, 3, 4, 4}
    print(my_set)
    ```

4. What will be printed?
    ```python
    print(int(True), float(False))
    print(True + True * False)
    print(2 + 3 * 4)
    print((2 + 3) * 4)
    print(2 ** 3 ** 2)
    print(10 > 5 > 2)
    print(10 > 5 < 2)
    ```

5. What is the output of:
    ```python
    a = 5
    b = 2
    print(a / b)
    print(a // b)
    print(a % b)
    ```

6. What is the output?
    ```python
    a = [1, 2, 3]
    b = a
    b[0] = 100
    print(a)
    ```

7. What will be printed?
    ```python
    x = [1, 2, 3]
    y = x
    x = [4, 5, 6]
    print(y)
    ```
8. What will be the output?
    ```python
    l=[1,2,4,(4,5,6)]
    print(type(l))
    ```
9. What will be the output?
    ```python
    s=[1,2,4,{1,4,6,4,5,6}]
    print(s)
    ```
10. What will be the output?
    ```python
    s=[{1},{2},{4},{1,4,6,4,5,6}]
    print(s)
    ```
11. What will be the output?
    ```python
    x={4,3,9,1,[1,2,"Hi"]}
    print(x)
    ```
12. What will be the output?
    ```python
    x={4,3,9,1,1,{1,2,3,2,3}}
    print(x)
    ```
13. What will be the output?
    ```python
    x=[4,3,9,1,1,{'a':1,'b':2,'c':3,'d':2,'e':3}]
    print(x)
    ```
13. What will be the output?
    ```python
    x={4,3,9,1,1,{'a':1,'b':2,'c':3,'d':2,'e':3}}
    print(x)
    ```