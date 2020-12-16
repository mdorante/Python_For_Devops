#!/usr/bin/env python
'''
simple function that will run everytime this file is called by command line
or imported into another file
'''


def say_it():
    greeting = 'Hello'
    name = 'Manuel'
    message = f'{greeting} {name}'
    print(message)


say_it()
