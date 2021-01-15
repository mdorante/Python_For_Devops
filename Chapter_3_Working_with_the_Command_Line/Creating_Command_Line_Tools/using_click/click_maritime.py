#!/usr/bin/env python
'''
simple click example
'''
import click


@click.group()
def cli():
    pass


@click.group(help='Ship related commands')
def ships():
    pass


cli.add_command(ships)


@ships.command(help='Sail a ship')
def sail():
    ship_name = 'Your ship'
    print(f'{ship_name} has set sail!')


@ships.command(help='List all of the ships')
def list_ships():
    ships = ['Going Merry', 'Thousand Sunny', 'Victory Hunter', 'Baratie']
    print(f"Ships: {', '.join(ships)}")


@cli.command(help='Talk to a sailor')
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)


if __name__ == '__main__':
    cli()
