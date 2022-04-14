from animal import Animal
import pygame
import random


class Csheep(Animal):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(11)
        self.set_initiative(4)
        self.set_symbol('C')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'csheep.png'))

    def spawn(self, world, x, child):
        return Csheep(world, x, child)

    def action(self, world):
        n = world.get_n()
        c_pos = self.get_x()
        c_x = c_pos % n
        c_y = c_pos // n
        d_x = 0
        d_y = 0
        distance = -1
        found = False
        for specie in world.get_org():
            if specie.get_symbol() == '*':
                found = True
                pos = specie.get_x()
                x = pos % n
                y = pos // n
                delta_x = abs(c_x - x)
                delta_y = abs(c_y - y)
                sum1 = delta_x + delta_y
                if distance == -1 or sum1 < distance:
                    distance = sum1
                    d_x = x
                    d_y = y
        if found:
            if d_x > c_x:
                self.collision(world, c_pos + 1)
            elif d_x < c_x:
                self.collision(world, c_pos - 1)
            if d_x == c_x:
                if d_y > c_y:
                    self.collision(world, c_pos + n)
                elif d_y < c_y:
                    self.collision(world, c_pos - n)
        else:
            super().action(world)


