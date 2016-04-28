# Lab 4 - Dictionaries

## Exercises

### 1. Computing sums

Create the function `sums` that receives a list of integers as argument and returns a dictionary where the key "`odd`" contains the sum of all the odd integers in the list, the key "`even`" contains the sum of all the even integers in the list, and the key "`all`" contains the sum of all integers in the list.

```python
sums([1, 2, 3, 4, 5]) # => {'odd': 9, 'even': 6, 'all': 15}
```

### 2. Implementing "Five in a row"

#### a. Fixing the printing

At the top of the `main.py` file you can find the dictionary used to store the state of the game (stored in the `game` variable). As you can see, it already has some moves stored inside of it. However, when the game is printed out to the console, these moves aren’t shown. That’s because the function `get_cell_value` always returns " ".

Change the implementation of this function so it works according to the comments at the top of the function. When you’re done, the moves already added to the game should be shown in the console when you play it.

#### b. Adding new moves

When the user enters the coordinates for a new move, a call to the function `make_move` is made. However, this function hasn’t been implemented, so it doesn’t actually add the move to the game. This is the reason why only the moves added in the beginning is printed out to the console.

Change the implementation of this function so it works according to the comments at the top of the function. When you’re done, you should be able to see the moves you enter while playing the game.

#### c. Validating input (1)

When the user enters the coordinates of the cell, he might enter too low/high integers. To check this, the function `does_cell_exist` is called. However, at the moment, this function always returns `True`, so it consider all coordinates to be valid.

Change the implementation of this function so it works according to the comments at the top of the function. When you’re done, the user will be prompt to re-enter the coordinates each time he has entered invalid coordinates.

#### d. Validating the input (2)

Even though if the coordinates entered by the user are valid coordinates in the game, the cell at those coordinates might already contain a cross or a circle. To check this, the function `is_cell_free` is called. However, at the moment, this function always returns `True`, so it consider all cells to be free all the time.

Change the implementation of this function so it works according to the comments at the top of the function. When you’re done, the user will be prompt to re-enter the coordinates each time she has entered coordinates of a cell that already contains a cross or a circle.

#### e. Changing player

At the moment, only crosses can be added to the game. That’s because the function `get_next_players_turn` always returns "`X`".

Change the implementation of this function so it works according to the comments at the top of the function. When you’re done, crosses and circles should be added to the game every other move.

#### f. Finding the winner

At the moment, even when one of the players gets 5 in a row, the game continues. That’s because the function `get_winner` always returns `None`.

Change the implementation of this function so it works according to the comments at the top of the function. When you’re done, the game should end when there is a winner.

## Run

Run the exercises:

```sh
python3 exercises.py
```

Run the game:

```sh
python3 five-in-a-row/main.py
```
