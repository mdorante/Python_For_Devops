#!/usr/bin/env python
'''
simple cli tool that echoes the arg you pass
'''

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input')

    # add a positional argument
    parser.add_argument('message', help='Message to echo')

    # add an optional argument and store a true boolean value
    parser.add_argument('--twice', '-t', help='Do it twice',
                        action='store_true')
    args = parser.parse_args()

    print(args.message)
    if args.twice:
        print(args.message)
