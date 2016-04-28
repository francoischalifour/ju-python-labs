#!/usr/bin/env python3
# coding: utf-8
# Lab 5 - Company backup
# François Chalifour

import os
import sqlite3

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

DB_FILE = 'restored-employees.db'
BACKUP_FILE = 'backup.log'

connection = sqlite3.connect(os.path.join(__location__, DB_FILE))
cursor = connection.cursor()

table_name = 'employees'
table_fields = ['name', 'age', 'duty']
table_types = ['TEXT', 'INTEGER', 'TEXT']


def create_table():
    request = '''CREATE TABLE IF NOT EXISTS {} (
        {} {},
        {} {},
        {} {}
    )'''.format(
        table_name,
        table_fields[0],
        table_types[0],
        table_fields[1],
        table_types[1],
        table_fields[2],
        table_types[2],
    )

    cursor.execute(request)


def execute_requests(backup_data):
    for line in backup_data:
        command, data = line.split(': ')

        if command.startswith('INSERT'):
            name, age, duty = data.split(', ')
            values = [repr(name), repr(age), repr(duty)]
            request = '''INSERT INTO {} ({}) VALUES ({})'''.format(
                    table_name,
                    ', '.join(table_fields),
                    ', '.join(values)
                )
        elif command.startswith('UPDATE'):
            name, field, value = data.split(', ')
            request = '''UPDATE {} SET {} = {!r} WHERE name = {!r}'''.format(
                    table_name,
                    field,
                    value,
                    name
                )
        elif command.startswith('DELETE'):
            name = data.split(', ')[0]
            request = '''DELETE FROM {} WHERE name = {!r}'''.format(
                    table_name,
                    name
                )

        cursor.execute(request)


def main():
    try:
        with open(os.path.join(__location__, BACKUP_FILE), 'r') as backup_file:
            backup_data = backup_file.read().split('\n')
            if os.stat(os.path.join(__location__, BACKUP_FILE)).st_size == 0:
                    raise(FileNotFoundError)
    except FileNotFoundError:
        print('The backup file is empty.')
    else:
        create_table()
        execute_requests(backup_data)

        connection.commit()
        connection.close()

if __name__ == '__main__':
    main()
