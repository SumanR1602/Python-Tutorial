#  Day 2 - Modules, Packages, and pip in Python

##  What is a Module?

A **module** is simply a Python file (`.py`) that contains functions, classes, or variables which you can import and reuse in other programs.

### Benefits:
- Reuse code instead of writing it again (avoid redundancy).
- Make programs more organized and maintainable.

**Note :** If you try to import the module which doesn't esxist it throws ModuleNotFoundError

### Types of Modules

#### 1. **Built-in Modules**
- These come pre-installed with Python.
- Created by Python experts, tested for reliability.
- **Examples:** `math`, `random`, `os`, `sys`

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

#### 2. **External (Third-Party) Modules / Packages**
- Created by the community, not part of default Python.
- Need to be installed using pip.
- **Examples:** `pandas`, `numpy`, `matplotlib`, `requests`

---

###  You can also create your own module:

**math_utils.py**
```python
def add(a, b):
    return a + b
```

**main.py**
```python
import math_utils
print(math_utils.add(2, 3))  # Output: 5
```

---

## What is a Package?

A **package** is a collection of modules stored in a directory.  
The folder must contain a special file named `__init__.py` (even if empty). This tells Python: “This is a package.” It also Lets you control which modules or functions are available when the package is imported.

### Example Package Structure:
```
my_package/
    __init__.py
    math_utils.py
    string_utils.py
```

### Usage:
```python
from my_package import math_utils
print(math_utils.add(2, 3))
```

---

## Difference between Module and Package

| Module                | Package                                   |
|-----------------------|-------------------------------------------|
| A single `.py` file   | A collection of modules stored in a folder|
| Example: `math.py`    | Example: `numpy` (which itself has many modules)|

---

## pip – Python’s Package Manager

**pip** helps us install, upgrade, or uninstall external Python packages.

### Common pip Commands:
```sh
pip install pandas       # Install a package
pip uninstall pandas     # Remove a package
pip show pandas          # Show details of a package
pip list                 # List installed packages
```

#### Example:
```sh
pip install numpy
```

---

## Checking Available Modules & Packages

- **Built-in + Installed Modules:**
  ```python
  help("modules")
  ```

- **Installed External Packages Only:**
  ```sh
  pip list
  ```
- **To search for a specific package:**
  ```
  pip show package_name
  ```
- **To know all the pip commands**
  ```
  pip --help
  ```