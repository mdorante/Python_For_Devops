#!/usr/bin/env python
'''
simple wrapped function example
'''


def say_hi():
    print('Hiiiiiiiiiiii')


def my_decorator(wrapped_function):
    def wrapper():
        print('Something before the wrapped function')
        wrapped_function()
        print('Something after the wrapped function')
    return wrapper


func = my_decorator(say_hi)
func()
