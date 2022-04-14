from plant import Plant
import pygame
import random


class Guarana(Plant):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(0)
        self.set_initiative(0)
        self.set_symbol('+')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'guarana.png'))

    def spawn(self, world, x, child):
        return Guarana(world, x, child)

    def fight(self, world, attack, defend, old_x, new_x):
        text = ""
        text += defend.get_symbol() + " gets killed by " + attack.get_symbol()
        world.add_to_com(text)
        s = attack.get_strength() + 3
        attack.set_strength(s)
        super().fight(world, attack, defend, old_x, new_x)