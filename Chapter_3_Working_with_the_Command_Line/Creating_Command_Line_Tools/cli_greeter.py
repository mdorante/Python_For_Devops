#!/usr/bin/env python
'''
Simple cli greeting using sys.argv to read args
'''

import sys


def say_hi(target, age):
    message = f'Hello {target}, you are {age} years old!'
    print(message)


if __name__ == '__main__':
    name = 'default_name'
    age = 0

    if '--help' in sys.argv or '-h' in sys.argv:
        help_message = f'Usage: {sys.argv[0]} --name <NAME> --age <AGE>'
        print(help_message)
        sys.exit()

    if '--name' in sys.argv:
        # Get the index for the name arg
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--age' in sys.argv:
        # Get the index for the age arg
        age_index = sys.argv.index('--age') + 1
        if age_index < len(sys.argv):
            age = sys.argv[age_index]

    say_hi(name, age)
