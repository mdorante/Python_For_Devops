#!/usr/bin/env python
'''
simple click example
'''
import click


@click.command()
@click.option('--greeting', default='Hey', help='How do you want to greet?')
@click.option('--name', default='Manu', help='Who do you want to greet?')
def greet(greeting, name):
    print(f'{greeting} {name}')


if __name__ == '__main__':
    greet()
