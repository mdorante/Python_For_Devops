#!/usr/bin/env python
'''
ships cli using subparsers
'''
import argparse


def sail():
    ship_name = 'Your ship'
    print(f'{ship_name} is setting sail!')


def list_ships():
    ships = ['Going Merry', 'Thousand Sunny', 'Victory Hunter', 'Baratie']
    print(f"Ships: {', '.join(ships)}")


def greet(greeting, name):
    print(f'{greeting} {name}!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime control')
    parser.add_argument('--twice', '-t', help='Do it twice',
                        action='store_true')

    subparsers = parser.add_subparsers(dest='subs')

    ship_parser = subparsers.add_parser('ships', help='Ship related commands')
    ship_parser.add_argument('command', choices=['list', 'sail'])

    sailor_parser = subparsers.add_parser('sailor', help='Talk to a sailor')
    sailor_parser.add_argument('name', help='Sailors name')
    sailor_parser.add_argument(
        '--greeting', '-g', help='Greeting', default='Ahoy there')

    args = parser.parse_args()

    reps = 2 if args.twice else 1
    for _ in range(reps):
        if args.subs == 'sailor':
            greet(args.greeting, args.name)
        elif args.command == 'list':
            list_ships()
        else:
            sail()
