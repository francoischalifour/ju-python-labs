# Lab 3 - Lists

## Exercises

### 1. Finding the highest value

Create the function `highest` that receives a list of numbers as argument and returns the highest number in that list.

```python
highest([5, 3]) # => 5
highest([2, 8, 4, 3]) # => 8
highest([-2, -5]) # => -2
```

### 2. Counting occurrences

Create the function `count` that receives a list of integers as argument and returns a list of integers. In the returned list, the integer at each index represents the number of times that index appeared as a value in the received list.

```python
count([0, 1, 2]) # => [1, 1, 1]
count([1, 1, 1]) # => [0, 3]
count([5, 2, 4, 7, 4]) # => [0, 0, 1, 0, 2, 1, 0, 1]
```

### 3. Comparing two lists

Create the function `are_equal` that receives two lists of numbers as arguments and returns `True` if the numbers at each index in the two lists are equal, otherwise `False`.

```python
are_equal([1, 2, 3], [1, 2, 3]) # => True
are_equal([1, 2, 3], [1, 2, 2]) # => False
are_equal([1, 2, 3], [1, 2]) # => False
are_equal([1, 2], [1, 2, 3]) # => False
```

### 4. Comparing many lists

Create the function `are_nested_lists_equal` that receives a list containing lists of numbers and returns `True` if all the nested lists are equal, otherwise `False`.

```python
are_nested_lists_equal([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]) # => True
are_nested_lists_equal([
    [1, 2, 3],
    [1, 2, 2],
    [1, 2, 3]
]) # => False
```

### 5. Populate the first list

Create the function `change_to_highest` that receives a list as argument. The received list will contain lists of numbers, and the function should change the received list so it contains the highest values from the nested lists.

```python
the_list = [
    [1, 2, 3],
    [5, 4, 3],
    [2, 7, 6]
]
change_to_highest(the_list) # => None
the_list # => [3, 5, 7]
```

### 6. A less simple calculator

This exercise is a continuation of your simple calculator implementation from [lab 2](../lab2).

Add the operation `undo` to your simple calculator. It should (if possible) undo the user's last operation by restoring the value in memory to what it was before the last operation.

```
Enter initial memory value: 0
Enter operation (add/sub/mul/div/undo/quit): undo
There is nothing to undo.
Enter operation (add/sub/mul/div/undo/quit): add
Enter operand: 1
1 is stored in memory.
Enter operation (add/sub/mul/div/undo/quit): add
Enter operand: 2
3 is stored in memory.
Enter operation (add/sub/mul/div/undo/quit): undo
1 is stored in memory.
Enter operation (add/sub/mul/div/undo/quit): undo
0 is stored in memory.
Enter operation (add/sub/mul/div/undo/quit): undo
There is nothing to undo.
Enter operation (add/sub/mul/div/quit): quit
The program finished with 60 in memory.
```

### 7. Sorting

Create the function `sort` that receives a list of numbers and returns a new list where the numbers appear in increasing order.

```python
sort([1, 4, 3, 2]) # => [1, 2, 3, 4]
```

### 8. Power set

Create the function `power_set` that receives a set (a list of numbers) and returns a list containing all the subsets of that set.

```python
power_set([]) # => [[]]
power_set([1]) # => [[], [1]]
power_set([1, 2]) # => [[], [1], [2], [1, 2]]
power_set([1, 2, 3]) # =>[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
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
