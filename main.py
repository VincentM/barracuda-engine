#! /usr/bin/env python3

from barracuda.world import World
from barracuda.archetypes import create_actor

from time import sleep


if __name__ == '__main__':
    world = World()
    for letter in ['A', 'B', 'C', 'D', 'E']:
        create_actor(world.entity_manager, team='team-letters', name=letter)

    for digit in ['1', '2', '3', '4', '5']:
        create_actor(world.entity_manager, team='team-digits', name=digit)

    while True:
        world.step(0.1)
        sleep(2)
