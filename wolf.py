from animal import Animal
import pygame
import random


class Wolf(Animal):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(9)
        self.set_initiative(5)
        self.set_symbol('W')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'wolf.png'))

    def spawn(self, world, x, child):
        return Wolf(world, x, child)