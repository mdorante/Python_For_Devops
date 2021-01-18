#!/usr/bin/env python
'''
simple maritime CLI using fire
'''
import fire


class Ships():
    # command groups with subcommands can be defined using classes
    def sail(self):
        ship_name = 'Your ship'
        print(f'{ship_name} is setting sail!')

    def list(self):
        ships = ['Going Merry', 'Thousand Sunny', 'Victory Hunter', 'Baratie']
        print(f"Ships: {', '.join(ships)}")


def sailors(greeting, name):
    print(f'{greeting} {name}')


class Cli():
    # top level group containing command (sailors) and command groups (ships)
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == '__main__':
    fire.Fire(Cli)
