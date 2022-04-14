from plant import Plant
import pygame
import random


class Grass(Plant):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(0)
        self.set_initiative(0)
        self.set_symbol('#')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'5m8846s5ix601.png'))

    def spawn(self, world, x, child):
        return Grass(world, x, child)