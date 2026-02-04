# Conditional Statements - Python Practice

This folder contains Python programs demonstrating conditional statements and decision-making using `if`, `elif`, and `else` statements.

## Files Overview

### 1. **check_leap_year.py**

Determines if a given year is a leap year.

- **Logic**: A year is a leap year if:
  - It is divisible by 400, OR
  - It is divisible by 4 AND NOT divisible by 100
- **Input**: Year (integer)
- **Output**: Whether the year is a leap year or not

### 2. **check_max_num.py**

Finds the maximum number among two given numbers.

- **Logic**: Compares two numbers and prints the greater one
- **Input**: Two numbers (integers)
- **Output**: The larger of the two numbers

### 3. **even_or_odd.py**

Checks whether a given number is even or odd.

- **Logic**:
  - First validates that the number is positive
  - Uses modulo operator (%) to determine if even or odd
- **Input**: A number (integer)
- **Output**: Whether the number is even or odd

### 4. **gender_greeting.py**

Provides a greeting based on the user's gender.

- **Logic**: Takes gender as input and displays appropriate greeting
- **Input**: Gender (string: "male", "female", or other)
- **Output**: Personalized greeting (Sir/Mam/other)

### 5. **conditional_statement.py**

Checks voting eligibility based on age using nested conditionals.

- **Logic**:
  - Validates age (between 0 and 102)
  - Checks if person is 18 or older for voting eligibility
- **Input**: Age (integer)
- **Output**: Whether the person can vote or not

### 6. **tem_check.py**

Categorizes temperature ranges with multiple conditions.

- **Logic**: Uses multiple `elif` statements to categorize temperature:
  - Below 0°C: Freezing cold
  - 0-10°C: Very cold
  - 10-20°C: Cold
  - 20-30°C: Pleasant
  - 30-40°C: Hot
  - Above 40°C: Very hot
- **Input**: Temperature (integer in Celsius)
- **Output**: Temperature category

## Concepts Covered

- **If statements**: Single condition checks
- **If-Elif-Else chains**: Multiple conditions
- **Nested conditionals**: Conditions within conditions
- **Logical operators**: AND (`and`), OR (`or`)
- **Modulo operator**: For checking divisibility
- **Input validation**: Checking valid ranges

## Running the Programs

To run any program:

```bash
python filename.py
```

Example:

```bash
python check_leap_year.py
```

Then follow the prompts to enter your input.
