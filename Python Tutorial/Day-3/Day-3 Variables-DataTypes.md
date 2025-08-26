# 📘 Day 3 - Variables and Data Types in Python

---

## 1️. What is a Variable?

A **variable** is like a container that stores data or values.  
You can name it and use it later.

```python
age = 20        # 'age' is a variable storing the value 20
name = "Alice"  # 'name' stores the string "Alice"
```

- `age` → integer value
- `name` → string value

---

## 2️. What is a Data Type?

A **data type** tells Python what kind of data is stored in a variable.This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function

**Examples of data types:**
- Numbers → `int`, `float`, `complex`
- Text → `str`
- True/False → `bool`
- Collections → `list`, `tuple`, `set`, `dict`

---

## 3️. Types of Data Types

### 🔹 Numeric Types

| Type    | Example | Description      |
|---------|---------|------------------|
| int     | 10      | Whole numbers    |
| float   | 3.14    | Decimal numbers  |
| complex | 2+3j    | Complex numbers  |


### 🔹 Set Types

| Type      | Example                    | Mutable/Immutable |
|-----------|----------------------------|-------------------|
| set       | {1,2,3}                    | Mutable           |
| frozenset | frozenset([1,2,3])         | Immutable         |

### 🔹 Mapping Type

| Type | Example                  | Mutable/Immutable |
|------|--------------------------|-------------------|
| dict | {"a":1, "b":2}           | Mutable           |

### 🔹 Boolean Type

- `True` or `False`
- Used for logical conditions.

### 🔹 Sequence Types

| Type  | Example      | Mutable/Immutable |
|-------|--------------|-------------------|
| list  | [1,2,3]      | Mutable           |
| tuple | (1,2,3)      | Immutable         |
| str   | "Hello"      | Immutable         |

---

## 4️. Mutable vs Immutable

- **Mutable** → can change after creation  
  Example: `list`, `set`, `dict`

  ```python
  my_list = [1, 2, 3]
  my_list[0] = 10   # Changed! [10, 2, 3]
  ```

- **Immutable** → cannot change after creation  
  Example: `int`, `float`, `tuple`, `str`

  ```python
  name = "Alice"
  # name[0] = "a"   # ERROR, string cannot be changed
  ```

---

## 5️. `type()` Function

The `type()` function tells you the data type of a variable.

```python
x = 10
y = 3.14
z = [1, 2, 3]

print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'list'>
```

## Important Points

- **Variable Naming Rules:**
  - Must start with a letter or underscore (`_`)
  - Cannot start with a number
  - Can contain letters, numbers, and underscores
  - Case-sensitive (`Age` and `age` are different)

- **Dynamic Typing:**  
  Python variables can change type during execution:
  ```python
  x = 10
  x = "Now I'm a string"
  ```

- **None Type:**  
  `None` is a special type representing the absence of a value.
  ```python
  x = None
  print(type(x))  # <class 'NoneType'>
  ```