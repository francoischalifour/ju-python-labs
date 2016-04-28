# Lab 5 - Data storage

## Exercises

### 1. Writing to and reading from files

*This exercise is a continuation of [exercise 3.6](../lab3/calculator.py) (the calculator).*

Add the operation `store`, which saves the entire state of the calculator program to a file of your choice.

Add the operation `load`, which sets the state of the calculator program to a previous state that has been stored in a file through the store operation.

### 2. Using SQLite

A company has a database with the table `employees` consisting of the columns `name`, `age`, and `duty`. In the beginning, this table was empty, but with time, it has been populated with data about the employees. Each time the database executed a query, information about the query was also logged to a file (`backup.log`) as a backup, in case the database would ever be deleted by mistake. The format of the entries in the log file is one of the following:

```
INSERT: <name>, <age>, <duty>
UPDATE: <name>, <column-name>, <value>
DELETE: <name>
```

Here are the first 7 lines in the log file:

```
INSERT: Alice, 51, Artists
INSERT: Belle, 42, Boss
INSERT: Chloe, 33, Clown
UPDATE: Belle, age, 24
DELETE: Alice
INSERT: Daisy, 14, Trainee
UPDATE: Chloe, name, Clair
```

Your task is to create a program that restores the database from the logfile. Assume the log file is located in the same folder as your Python program. You can also assume that the names and duties only contain alphabetical letters (a-z and A-Z). The restored database should be saved in the file `restored-employees.db`. If the log file would only consist of the 7 lines shown above, the restored database table should look like the following:

| Name  | Age | Duty    |
|-------|-----|---------|
| Belle | 24  | Boss    |
| Clair | 33  | Clown   |
| Daisy | 14  | Trainee |

## Run

Run the calculator:

```sh
python3 calculator/calculator.py
```

Run the backup program:

```sh
python3 company/restore.py
```

See the result:

```sh
sqlite3
> .open restored-employees.db
> SELECT * FROM employees;
```
