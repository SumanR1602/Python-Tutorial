#  Day 2 - Comments, Escape Sequences & Print in Python

---

##  Comments in Python

Comments are notes in your code that Python ignores during execution. They help humans understand the code better.They are used to explain a block of code.

###  Single-line Comments

Use `#` for single-line comments.

```python
# This is a single-line comment
print("Hello, Python!")  # You can also write a comment after code
```

###  Multi-line Comments

Use triple quotes (`'''` or `"""`) for multi-line comments.

```python
'''
This is a multi-line comment
that can span multiple lines.
'''
print("Learning Python is fun!")
```

#### ⌨ Shortcut for Comments (Windows)

To quickly comment/uncomment code: **Ctrl + /**

---

##  Escape Sequence Characters

Escape sequence characters allow you to insert special characters into strings that are otherwise difficult or impossible to type directly.

An escape sequence starts with a backslash (`\`) followed by a character.  
For example, to include a double quote inside a string that is enclosed in double quotes, you use `\"`:

```python
# This will cause an error:
# print("This doesn't "execute""')

# Correct usage with escape sequence:
print("This will \"execute\"")
```

| Escape Code | Meaning                        |
|-------------|-------------------------------|
| `\n`        | New line                      |
| `\t`        | Tab (adds extra spaces)       |
| `\\`        | Prints a backslash (`\`)      |
| `\'`        | Prints a single quote (`'`)   |
| `\"`        | Prints a double quote (`"`)   |

**Examples:**

```python
print("Hello\nWorld")    # Prints Hello on one line, World on the next line
print("Name:\tAdam")     # Adds a tab space after Name:
print("She said, \"Hi!\"")  # Prints double quotes inside the string
print('It\'s Python!')      # Prints single quote inside the string
print("C:\\Users\\Adam")    # Prints a file path
```

---

##  The print() Function – Special Parameters

The `print()` function has some useful arguments:

- **sep** → Defines how multiple items are separated (default: space `" "`).
- **end** → Defines what to print at the end (default: newline `\n`).

**Example:**

```python
print("hello", 3, 4, sep='-', end='*')
```

**Output:**
```
hello-3-4*
```

Here,

- `sep='-'` → separates values with `-` instead of space.
- `end='*'` → ends the line with `*` instead of moving to