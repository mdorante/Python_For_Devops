#!/usr/bin/env python
'''
simple decorator example
'''


def my_decorator(wrapped_function):
    def wrapper():
        print('Something before the wrapped function')
        wrapped_function()
        print('Something after the wrapped function')
    return wrapper


@my_decorator
def say_hi():
    print('Hiiiiiiiiiiii')


say_hi()
