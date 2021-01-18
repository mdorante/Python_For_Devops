#!/usr/bin/env python
'''
simple fire example
fire creates a introspective, minimal CLI UI for any function you want to expose
'''
import fire


def greet(greeting='Hey', name='Dude'):
    print(f'{greeting} {name}')


if __name__ == '__main__':
    fire.Fire(greet)
