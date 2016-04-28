# Lab 6 - Object-Oriented Programming

## Exercises

### 1. Representing the calculator as a class

*This exercise is a continuation of [exercise 5.1](../lab5/calculator.py) (the calculator).*

Change your code so the calculator is represented as a class. The calculator should have one method for each corresponding command the user can enter. The main program should then use this class.

### 2. Representing the *Five in a Row game* as a class

*This exercise is a continuation of [exercise 4.2](../lab4/five-in-a-row) (the Five in a Row game).*

Change your code so the game is represented as a class. All functions you implemented in exercise 4.2 should now be methods in this class, and the `game` variable in the main program should of course no longer store a dictionary, but an instance of this class.

The game state is not the only thing that can be represented by a class. Each move in the game can be represented by a class, and the list containing all made moves can also be represented by a class. Implement at least one of these as a class.

## Run

Run the calculator:

```sh
python3 calculator/calculator.py
```

Run the game:

```sh
python3 five-in-a-row/main.py
```
