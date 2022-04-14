from animal import Animal
import pygame
import random


class Turtle(Animal):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(2)
        self.set_initiative(1)
        self.set_symbol('T')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'turtle.png'))

    def spawn(self, world, x, child):
        return Turtle(world, x, child)

    def action(self, world):
        chance = random.randint(0, 3)
        if chance == 0:
            super().action(world)

    def fight(self, world, attack, defend, old_x, new_x):
        text = ""
        if defend.get_symbol() == 'T':
            if attack.get_strength() >= 5:
                text += defend.get_symbol() + " gets killed by " + attack.get_symbol()
                world.add_to_com(text)
                self.kill(world, defend)
                attack.set_x(new_x, world, old_x)
            else:
                text += defend.get_symbol() + " defends from " + attack.get_symbol()
                world.add_to_com(text)
        else:
            super().fight(world, attack, defend, old_x, new_x)