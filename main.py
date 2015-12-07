#! /usr/bin/env python3

from barracuda.world import World
from barracuda.archetypes import create_actor

from time import sleep


if __name__ == '__main__':
    world = World()
    create_actor(world.entity_manager, team='team-1', name='A')
    create_actor(world.entity_manager, team='team-2', name='B')
    create_actor(world.entity_manager, team='team-1', name='C')
    while True:
        world.step(0.1)
        sleep(0.1)
