# Lab 1 - Mathematical functions

## Exercises

### 1. Factorial

Create the function `factorial` which receives an integer as argument and returns the factorial for that integer. You can presume the integer to be non-negative.

```python
factorial(0) # => 1
facotrial(7) # => 5040
```

### 2. Exponentiation

Create the function `exp` which receives two integers as arguments and returns the first argument to the power of the second argument. You can presume the second argument to be non-negative.

```python
exp(5, 0) # => 1
exp(2, 1) # => 2
exp(2, 2) # => 4
exp(2, 3) # => 8
exp(2, -2) # => 0.25
```

### 3. A different sum

Based on the example usage below, create the function `sum`. You can presume the argument to be a non-negative integer.

```python
sum(1) # => 1
sum(2) # => 1 + (2 + 2) => 5
sum(3) # => 1 + (2 + 2) + (3 + 3 + 3) => 14
sum(4) # => 1 + (2 + 2) + (3 + 3 + 3) + (4 + 4 + 4 + 4) => 30
```

### 4. Summering integers

Create the function `sum_of_ints` which receives two integers as arguments and returns the sum of the integers between these two integers. You can presume the first integer to be smaller than the second.

```python
sum_of_ints(0, 4) # => 10
sum_of_ints(10, 11) # => 21
sum_of_ints(7, 7) # => 7
sum_of_ints(-2, 2) # => 0
sum_of_ints(-4, 0) # => -10
```

### 5. Combinations
Create the function `combinations` which receives two integers as arguments (call them `n` and `k`) and returns the number of combinations (order doesn’t matter) you can create by picking `k` elements from `n` elements.

You can presume the arguments to be non-negative integers and `k` < `n`.

```python
combinations(5, 0) # => 1
combinations(5, 1) # => 5
combinations(5, 2) # => 10
combinations(5, 3) # => 10
combinations(5, 4) # => 5
combinations(5, 5) # => 1
```

## Run

Run the exercises:

```sh
python3 exercises.py
```
