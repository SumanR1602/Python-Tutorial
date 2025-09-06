# Day 4 - Type Casting in Python


## What is Type Casting?
The conversion of one data type into the other data type is known as **type casting** in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

For example: Converting an `int` to a `float`, or a `string` to an `int`.

```python
x = "100"        # string
y = int(x)       # converted to integer
print(y, type(y))
```

**Output:**
```
100 <class 'int'>
```

---

## Why Do We Use Type Casting?

- To match data types in operations (e.g., adding an `int` to a `string` is not allowed).
- To accept user input (input is always a string by default, so you may need to convert it to `int` or `float`).
- To format data for calculations or output.

**Example:**
```python
a = input("Enter a number: ")  # input is string
b = int(a) + 5                 # convert to int for math
print(b)
```

---

## Types of Type Casting

### 1. Implicit Type Casting (Automatic Conversion)

- Done automatically by Python.
- Python converts a smaller data type into a larger data type to avoid data loss.

**Example:**
```python
x = 10       # int
y = 2.5      # float
z = x + y    # int + float → float
print(z, type(z))
```
**Output:**
```
12.5 <class 'float'>
```
Here, `int` is automatically converted to `float`.

---

### 2. Explicit Type Casting (Manual Conversion)

- The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

**Common casting functions:**
- `int()` → Converts to integer
- `float()` → Converts to float
- `str()` → Converts to string
- `list()` → Converts to list
- `tuple()` → Converts to tuple
- `set()` → Converts to set

**Example:**
```python
a = "25"
b = int(a)      # string → int
c = float(b)    # int → float
print(b, type(b))
print(c, type(c))
```
**Output:**
```
25 <class 'int'>
25.0 <class 'float'>
```

---
**Note:** Not all conversions are possible:
  Trying to convert a non-numeric string to `int` or `float` will cause an error.
  ```python
  x = "abc"
  y = int(x)  # ValueError!
  ```

## Summary Table

| Function   | Converts To | Example                | Result         |
|------------|-------------|------------------------|---------------|
| `int(x)`   | Integer     | `int("10")`            | `10`          |
| `float(x)` | Float       | `float("3.14")`        | `3.14`        |
| `str(x)`   | String      | `str(100)`             | `"100"`       |
| `list(x)`  | List        | `list((1,2,3))`        | `[1, 2, 3]`   |
| `tuple(x)` | Tuple       | `tuple([1,2,3])`       | `(1, 2, 3)`   |
| `set(x)`   | Set         | `set([1,2,2,3])`       | `{1, 2, 3}`   |

---
