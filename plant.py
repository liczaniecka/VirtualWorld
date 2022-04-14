from abc import ABC
from organism import Organism
import random


class Plant(Organism, ABC):

    def action(self, world):
        self.reproduction(world)

    def reproduction(self, world):
        sow = random.randint(0, 9)  # 10% chance of sowing
        if sow == 0:
            direction = random.randint(0, 3)
            w_map = world.get_map()
            n = world.get_n()
            m = world.get_m()
            x = self.get_x()
            if direction == 0:
                if x - n >= 0:
                    if w_map[x - n] == 0:
                        z = x - n
                        child = self.spawn(world, z, True)
                        world.add_to_org(child)
                else:
                    self.action(world)
            elif direction == 1:
                if x % n != n - 1:
                    if w_map[x + 1] == 0:
                        z = x + 1
                        child = self.spawn(world, z, True)
                        world.add_to_org(child)
                else:
                    self.action(world)
            elif direction == 2:
                if x + n < n * m:
                    if w_map[x + n] == 0:
                        z = x + n
                        child = self.spawn(world, z, True)
                        world.add_to_org(child)
                else:
                    self.action(world)
            elif direction == 3:
                if x % n != 0:
                    if w_map[x - 1] == 0:
                        z = x - 1
                        child = self.spawn(world, z, True)
                        world.add_to_org(child)
                else:
                    self.action(world)

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
            world.get_map()[old_x] = 0
