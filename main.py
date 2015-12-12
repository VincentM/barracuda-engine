#! /usr/bin/env python3

from time import sleep
import argparse

from barracuda.world import World
from barracuda.archetypes import create_actor


def main():
    parser = argparse.ArgumentParser(description='Barracuda demo')
    parser.add_argument('--load', '-l', help='Load saved world')
    parser.add_argument('--save', '-s',
                        help='Save the world at the end of the iterations')
    parser.add_argument('---iterations', '-n', type=int,
                        help='Number of iterations before exiting')
    args = parser.parse_args()
    world = World()
    if args.load:
        print('Loading %s' % args.load)
        world.load(args.load)
    else:
        for letter in ['A', 'B', 'C', 'D', 'E']:
            create_actor(world.entity_manager, team='team-letters', name=letter)

        for digit in ['1', '2', '3', '4', '5']:
            create_actor(world.entity_manager, team='team-digits', name=digit)
    i = 0
    while True:
        world.step(0.1)
        i += 1
        if args.iterations and i == args.iterations:
            break
        sleep(2)
    if args.save:
        print('Saving world as %s' % args.save)
        world.save(args.save)


if __name__ == '__main__':
    main()
