from animal import Animal
from plant import Plant
import pygame
import random


class Hogweed(Plant):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(10)
        self.set_initiative(0)
        self.set_symbol('*')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'hogweed.png'))

    def spawn(self, world, x, child):
        return Hogweed(world, x, child)

    def kill_others(self, world):
        n = world.get_n()
        m = world.get_m()
        pos = self.get_x()
        up = pos - n
        right = pos + 1
        down = pos + n
        left = pos - 1
        text = ""
        if up > 0 and isinstance(world.get_map()[up], Animal):
            specie = world.get_map()[up]
            if specie.get_symbol() != "C":
                text += specie.get_symbol() + " gets killed by *"
                world.add_to_com(text)
                self.kill(world, specie)
        if right % n != n - 1 and isinstance(world.get_map()[right], Animal):
            specie = world.get_map()[right]
            if specie.get_symbol() != "C":
                text += specie.get_symbol() + " gets killed by *"
                world.add_to_com(text)
                self.kill(world, specie)
        if down < n * m and isinstance(world.get_map()[down], Animal):
            specie = world.get_map()[down]
            if specie.get_symbol() != "C":
                text += specie.get_symbol() + " gets killed by *"
                world.add_to_com(text)
                self.kill(world, specie)
        if left % n != 0 and isinstance(world.get_map()[left], Animal):
            specie = world.get_map()[left]
            if specie.get_symbol() != "C":
                text += specie.get_symbol() + " gets killed by *"
                world.add_to_com(text)
                self.kill(world, specie)

    def action(self, world):
        self.reproduction(world)
        self.kill_others(world)

    def fight(self, world, attack, defend, old_x, new_x):
        text = ""
        if attack.get_symbol() != "C":
            text += attack.get_symbol() + " gets killed by *"
            world.add_to_com(text)
            self.kill(world, attack)
            self.kill(world, defend)
        else:
            self.kill(world, defend)
            text += "* gets killed by C"
            world.add_to_com(text)
            attack.set_x(new_x, world, old_x)