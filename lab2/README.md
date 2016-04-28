# Lab 2 - Basic functions

## Exercises

### 1. Absolute value

Create the function `abs` that receives a number as argument and returns the absolute value of that number.

```python
abs(5) # => 5
abs(-5) # => 5
abs(0) # => 0
```

### 2. Closest to zero

Create the function `closest_to_zero` that receives two numbers as arguments and returns the number that is closest to 0.

```python
closest_to_zero(5, 9) # => 5
closest_to_zero(3, -2) # => -2
closest_to_zero(2, 2) # => 2
```

### 3. Closest to zero (2)

Create the function `closest_to_zero_4` that receives four numbers as arguments and returns the number that is closest to 0.

```python
closest_to_zero_4(5, 9, 2, 11) # => 2
closest_to_zero_4(0, 3, -2, 4) # => 0
closest_to_zero_4(2, 2, -2, 1) # => 1
```

### 4. Closest to zero (3)

Create the function `closest_to_zero_10` that receives ten numbers as arguments and returns the number that is closest to 0.

```python
closest_to_zero_10(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # => 1
```

### 5. String with numbers

Based on the example usage below, create the function `string_with_numbers`.

```python
string_with_numbers(3) # => '1_2_3'
string_with_numbers(5) # => '1_2_3_4_5'
```

### 6. A simple calculator

Create a small program that functions as a simple calculator with a number in memory for which you can add, subtract, multiply and divide other integers. Example usage (the text shown has been copied from a terminal/command line where the program has run, and the text in bold represents text entered by the user):

```
Enter initial memory value: 0
Enter operation (add/sub/mul/div/quit): add
Enter operand: 20
20 is stored in memory.
Enter operation (add/sub/mul/div/quit): mul
Enter operand: 3
60 is stored in memory.
Enter operation (add/sub/mul/div/quit): quit
The program finished with 60 in memory.
```

## Run

Run the exercises:

```sh
python3 exercises.py
```

Run the calculator:

```sh
python3 calculator.py
```

Run the tests:

```sh
python3 tests.py
```
