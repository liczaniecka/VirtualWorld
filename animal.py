from abc import ABC
from organism import Organism
from random import randint
from plant import Plant


class Animal(Organism, ABC):

    def action(self, world):
        direction = randint(0, 3)
        n = world.get_n()
        m = world.get_m()
        x = self.get_x()
        if direction == 0:  # up
            if x - n >= 0:
                self.collision(world, x - n)
            else:
                self.action(world)
        elif direction == 1:  # right
            if x % n != n - 1:
                self.collision(world, x + 1)
            else:
                self.action(world)
        elif direction == 2:  # down
            if x + n < n * m:
                self.collision(world, x + n)
            else:
                self.action(world)
        elif direction == 3:  # left
            if x % n != 0:
                self.collision(world, x - 1)
            else:
                self.action(world)

    def collision(self, world, new_x):
        if not isinstance(world.get_map()[new_x], Organism):
            self.set_x(new_x, world, self.get_x())
        elif world.get_map()[new_x].get_symbol() != self.get_symbol():
            world.get_map()[new_x].fight(world, self, world.get_map()[new_x], self.get_x(), new_x)
        elif world.get_map()[new_x].get_symbol() == self.get_symbol() and world.get_map()[new_x].get_symbol() != 'H' and self.get_symbol() != 'H':
            self.reproduction(world, world.get_map()[new_x], new_x)

    @staticmethod
    def reproduction(world, parent, new_x):
        if parent.get_age() >= 3:
            n = world.get_n()
            m = world.get_m()
            if new_x - n >= 0 and world.get_map()[new_x - n] == 0:
                child = parent.spawn(world, new_x - n, True)
                world.add_to_org(child)
            elif new_x % n != n - 1 and world.get_map()[new_x + 1] == 0:
                child = parent.spawn(world, new_x + 1, True)
                world.add_to_org(child)
            elif new_x + n < n * m and world.get_map()[new_x + n] == 0:
                child = parent.spawn(world, new_x + n, True)
                world.add_to_org(child)
            elif new_x % n != 0 and world.get_map()[new_x - 1] == 0:
                child = parent.spawn(world, new_x - 1, True)
                world.add_to_org(child)

    def fight(self, world, attack, defend, old_x, new_x):
        text = ""
        if attack.get_strength() >= defend.get_strength():
            text += defend.get_symbol() + " gets killed by " + attack.get_symbol()
            world.add_to_com(text)
            self.kill(world, defend)
            attack.set_x(new_x, world, old_x)
        else:
            text += attack.get_symbol() + " gets killed by " + defend.get_symbol()
            world.add_to_com(text)
            self.kill(world, attack)

