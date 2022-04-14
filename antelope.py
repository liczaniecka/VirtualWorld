from animal import Animal
import pygame
import random
MOVES = 2


class Antelope(Animal):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(4)
        self.set_initiative(4)
        self.set_symbol('A')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'antelope.png'))

    def spawn(self, world, x, child):
        return Antelope(world, x, child)

    def action(self, world):
        for i in range(MOVES):
            super().action(world)

    def fight(self, world, attack, defend, old_x, new_x):
        if defend.get_symbol() == 'A':
            escape = random.randint(0, 1)
            n = world.get_n()
            m = world.get_m()
            w_map = world.get_map()
            text = ""
            if escape == 0:  # no escape
                super().fight(world, attack, defend, old_x, new_x)
            elif escape == 1:
                if new_x - n >= 0 and w_map[new_x - n] == 0:
                    text += self.get_symbol() + " has escaped "
                    world.add_to_com(text)
                    defend.set_x(new_x - n, world, old_x)
                elif new_x % n != n - 1 and w_map[new_x + 1] == 0:
                    text += self.get_symbol() + " has escaped "
                    world.add_to_com(text)
                    defend.set_x(new_x + 1, world, old_x)
                elif new_x + n < n * m and w_map[new_x + n] == 0:
                    text += self.get_symbol() + " has escaped "
                    world.add_to_com(text)
                    defend.set_x(new_x + n, world, old_x)
                elif new_x % n != 0 and w_map[new_x - 1] == 0:
                    text += self.get_symbol() + " has escaped "
                    world.add_to_com(text)
                    defend.set_x(new_x - 1, world, old_x)
                else:
                    super().fight(world, attack, defend, old_x, new_x)
        else:
            super().fight(world, attack, defend, old_x, new_x)


