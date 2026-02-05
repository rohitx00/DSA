# Python Loops

## Overview

Loops are fundamental programming constructs that allow you to execute a block of code repeatedly without writing it multiple times. They help in iterating over sequences, processing data, and automating repetitive tasks.

## Types of Loops in Python

### 1. **For Loop**

A `for` loop iterates over a sequence (list, tuple, string, range, etc.) and executes the code block for each item.

**Syntax:**

```python
for variable in sequence:
    # code to execute
```

**Key Features:**

- Used when you know the number of iterations in advance
- Automatically iterates through each element in a sequence
- Works with strings, lists, tuples, dictionaries, sets, and ranges

**Example:**

```python
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4
```

### 2. **While Loop**

A `while` loop executes a block of code as long as a condition is true.

**Syntax:**

```python
while condition:
    # code to execute
```

**Key Features:**

- Useful when you don't know how many iterations are needed
- Continues until the condition becomes false
- Requires manual increment/decrement of the loop variable
- Risk of infinite loops if condition never becomes false

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 3. **Nested Loops**

Loops within loops, used for working with multi-dimensional data structures.

**Example:**

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")  # Creates a 3x3 matrix pattern
```

## Loop Control Statements

### **Break Statement**

Terminates the loop immediately when executed.

```python
for i in range(10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(i)
```

### **Continue Statement**

Skips the current iteration and moves to the next one.

```python
for i in range(5):
    if i == 2:
        continue  # Skips printing 2
    print(i)
```

### **Pass Statement**

Used as a placeholder when a statement is required but no action is needed.

```python
for i in range(5):
    if i == 3:
        pass  # Does nothing
    print(i)
```

### **Else Clause with Loops**

Executes when the loop completes normally (without break).

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

## Common Loop Use Cases

1. **Iterating through lists/arrays**

   ```python
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       print(num)
   ```

2. **Range-based iteration**

   ```python
   for i in range(1, 10, 2):  # Start: 1, Stop: 10, Step: 2
       print(i)  # Prints: 1, 3, 5, 7, 9
   ```

3. **String iteration**

   ```python
   for char in "Hello":
       print(char)
   ```

4. **Dictionary iteration**

   ```python
   person = {"name": "John", "age": 25}
   for key, value in person.items():
       print(f"{key}: {value}")
   ```

5. **Pattern printing**
   ```python
   for i in range(1, 5):
       for j in range(i):
           print("*", end="")
       print()  # New line
   ```

## Key Differences: For vs While

| Feature                 | For Loop              | While Loop             |
| ----------------------- | --------------------- | ---------------------- |
| **Best Used For**       | Known iterations      | Unknown iterations     |
| **Syntax**              | for item in sequence  | while condition        |
| **Automatic increment** | Yes (for each item)   | Manual required        |
| **Infinite loop risk**  | Low                   | High                   |
| **Common use**          | Iterating collections | Conditions-based loops |

## Best Practices

1. Use `for` loops when iterating over sequences
2. Use `while` loops for condition-based iteration
3. Keep loop conditions simple and clear
4. Avoid infinite loops by ensuring the exit condition can be met
5. Use `break` and `continue` carefully to avoid confusing logic
6. Use meaningful variable names in loops
7. Consider using list comprehensions for simple transformations

## Running Loop Programs

To run any loop program:

```bash
python filename.py
```

Example:

```bash
python for_loop_example.py
```
