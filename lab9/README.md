# Lab 9 - Functional programming

In this lab, you must use functional programming; you are not allowed to use statements/expressions with side effects (such as loops, list comprehension, re-assignments, etc.).

## Exercises

### 1. Multiplying numbers

Create the function `product_between` that receives two integers as arguments (the first one lower than the second) and returns the product of the integers between these two numbers.

```python
product_between(1, 3) # => 6
product_between(10, 10) # => 10
product_between(5, 7) # => 210
```

### 2. Summarizing numbers in lists

Create the function `sum_of_numbers` that receives a list of numbers as arguments and returns the sum of all the numbers in the list.

```python
sum_of_numbers([]) # => 0
sum_of_numbers([1, 1, 1]) # => 3
sum_of_numbers(3, 1, 2) # => 6
```

### 3. Searching for a value in a list

Create the function `is_in_list` which receives a number and a list of numbers as arguments and returns `True` if the list contains the number, otherwise `False`.

```python
is_in_list(1, []) # => False
is_in_list(3, [1, 2, 3, 4, 5]) # => True
is_in_list(7, [1, 2, 1, 2]) # => False
```

### 4. Counting elements in lists

Create the function `count` that receives a list of numbers and a number as arguments, and returns the number of time the number occurs in the list.

```python
count([], 4) # => 0
count([1, 2, 3, 4, 5], 3) # => 1
count([1, 1, 1], 1) # => 3
```

## Run

```sh
python3 exercises.py
```
