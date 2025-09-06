# Day 4 - Operators in Python

##  What is an Operator?

An **operator** is a symbol that performs operations on variables and values.

**Example:**
```python
a = 10
b = 5
print(a + b)  # + is an operator, output: 15
```

---

## Types of Operators in Python

### 1️. Arithmetic Operators – Perform Math Operations

| Operator | Meaning         | Example   | Output |
|----------|----------------|-----------|--------|
| `+`      | Addition       | 5 + 3     | 8      |
| `-`      | Subtraction    | 5 - 3     | 2      |
| `*`      | Multiplication | 5 * 3     | 15     |
| `/`      | Division       | 5 / 2     | 2.5    |
| `//`     | Floor Division | 5 // 2    | 2      |
| `%`      | Modulus        | 5 % 2     | 1      |
| `**`     | Exponent       | 5 ** 2    | 25     |

---

### 2️. Comparison Operators – Compare Values (Return True or False)

| Operator | Meaning         | Example   | Output |
|----------|----------------|-----------|--------|
| `==`     | Equal to       | 5 == 3    | False  |
| `!=`     | Not equal to   | 5 != 3    | True   |
| `>`      | Greater than   | 5 > 3     | True   |
| `<`      | Less than      | 5 < 3     | False  |
| `>=`     | Greater or eq. | 5 >= 5    | True   |
| `<=`     | Less or eq.    | 5 <= 3    | False  |

---

### 3️. Logical Operators – Combine Boolean Conditions

| Operator | Meaning                  | Example           | Output |
|----------|--------------------------|-------------------|--------|
| `and`    | True if both are True    | True and False    | False  |
| `or`     | True if any is True      | True or False     | True   |
| `not`    | Reverse the Boolean      | not True          | False  |

---

### 4️. Assignment Operators – Assign Values

| Operator | Example    | Meaning         |
|----------|------------|-----------------|
| `=`      | x = 5      | Assign value    |
| `+=`     | x += 2     | x = x + 2       |
| `-=`     | x -= 2     | x = x - 2       |
| `*=`     | x *= 2     | x = x * 2       |
| `/=`     | x /= 2     | x = x / 2       |
| `%=`     | x %= 2     | x = x % 2       |
| `**=`    | x **= 2    | x = x ** 2      |
| `//=`    | x //= 2    | x = x // 2      |

---

### 5️. Bitwise Operators – Work on Bits

| Operator | Meaning      | Example   | Output |
|----------|-------------|-----------|--------|
| `&`      | AND         | 5 & 3     | 1      |
| `\|`      | OR          | 5 &#124; 3| 7      |
| `^`      | XOR         | 5 ^ 3     | 6      |
| `~`      | NOT         | ~5        | -6     |
| `<<`     | Left shift  | 5 << 1    | 10     |
| `>>`     | Right shift | 5 >> 1    | 2      |

---

### 6️. Membership Operators – Check Presence in a Sequence

| Operator | Meaning                  | Example             | Output |
|----------|--------------------------|---------------------|--------|
| `in`     | True if value present    | 3 in [1,2,3]        | True   |
| `not in` | True if value not present| 4 not in [1,2,3]    | True   |

---

### 7️. Identity Operators – Check if Objects are the Same

| Operator | Meaning                  | Example   | Output      |
|----------|--------------------------|-----------|-------------|
| `is`     | True if same object      | a is b    | True/False  |
| `is not` | True if not same object  | a is not b| True/False  |


**Note** : Always use parentheses `()` to clarify complex expressions and avoid confusion.