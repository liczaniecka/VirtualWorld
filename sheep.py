from animal import Animal
import pygame
import random


class Sheep(Animal):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(4)
        self.set_initiative(4)
        self.set_symbol('S')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'sheep.png'))

    def spawn(self, world, x, child):
        return Sheep(world, x, child)