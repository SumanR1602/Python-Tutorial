# `elif` in Python

The **`elif`** (short for "else if") statement in Python allows you to check **multiple conditions** in sequence.  

It comes after an `if` statement and before an optional `else` statement.

---

## Basic Syntax

```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition2 is True (and condition1 was False)
elif condition3:
    # Runs if condition3 is True (and previous were False)
else:
    # Runs if none of the above conditions are True

```
## Example

```python
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")
elif temperature > 10:
    print("It's cool outside.")
else:
    print("It's cold outside.")
```

**Output:**
```
It's warm outside.
```