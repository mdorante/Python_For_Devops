#!/usr/bin/env python
'''
File execution example. 
say_it() will only run if this file is called directly from the command line
'''


def say_it():
    greeting = 'Hello'
    name = 'Manuel'
    message = f'{greeting} {name}'
    print(message)


if __name__ == '__main__':
    say_it()
