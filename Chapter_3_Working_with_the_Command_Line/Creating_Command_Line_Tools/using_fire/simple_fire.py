#!/usr/bin/env python
'''
another simple fire example
'''
import fire


def greet(greeting='Hey', name='Dude'):
    print(f'{greeting} {name}')


def bye(goodbye='Bye', name='Dude'):
    print(f'{goodbye} {name}')


# you can group all functions as subcommands to the file by invoking Fire() with no arguments
if __name__ == '__main__':
    fire.Fire()
