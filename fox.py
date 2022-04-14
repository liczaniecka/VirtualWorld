from animal import Animal
import pygame
import random


class Fox(Animal):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(3)
        self.set_initiative(7)
        self.set_symbol('F')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'fox.png'))

    def spawn(self, world, x, child):
        return Fox(world, x, child)

    def action(self, world):
        direction = random.randint(0, 3)
        n = world.get_n()
        m = world.get_m()
        x = self.get_x()
        if direction == 0:  # up
            if x - n >= 0:
                if world.get_map()[x - n] == 0:
                    self.collision(world, x - n)
                else:
                    if world.get_map()[x - n].get_strength() <= self.get_strength():
                        self.collision(world, x - n)
            else:
                self.action(world)
        elif direction == 1:  # right
            if x % n != n - 1:
                if world.get_map()[x + 1] == 0:
                    self.collision(world, x + 1)
                else:
                    if world.get_map()[x + 1].get_strength() <= self.get_strength():
                        self.collision(world, x + 1)
            else:
                self.action(world)
        elif direction == 2:  # down
            if x + n < n * m:
                if world.get_map()[x + n] == 0:
                    self.collision(world, x + n)
                else:
                    if world.get_map()[x + n].get_strength() <= self.get_strength():
                        self.collision(world, x + n)
            else:
                self.action(world)
        elif direction == 3:  # left
            if x % n != 0:
                if world.get_map()[x - 1] == 0:
                    self.collision(world, x - 1)
                else:
                    if world.get_map()[x - 1].get_strength() <= self.get_strength():
                        self.collision(world, x - 1)
            else:
                self.action(world)
