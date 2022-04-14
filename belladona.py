from plant import Plant
import pygame
import random


class Belladona(Plant):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(99)
        self.set_initiative(0)
        self.set_symbol('!')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'belladonna.png'))

    def spawn(self, world, x, child):
        return Belladona(world, x, child)

    def fight(self, world, attack, defend, old_x, new_x):
        text = ""
        text += attack.get_symbol() + " gets killed by " + attack.get_symbol()
        world.add_to_com(text)
        self.kill(world, attack)
        self.kill(world, defend)