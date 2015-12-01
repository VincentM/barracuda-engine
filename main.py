#! /usr/bin/env python3

from barracuda.world import World
from time import sleep


if __name__ == '__main__':
    world = World()
    while True:
        world.step(0.1)
        sleep(0.1)
