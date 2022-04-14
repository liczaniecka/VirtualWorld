from abc import ABC, abstractmethod
import random


class Organism(ABC):

    __strength = 0
    __initiative = 0
    __pos_x = 0
    __symbol = '?'
    __age = 0
    __alive = True
    __image = 0

    @abstractmethod
    def action(self, world):
        pass

    @abstractmethod
    def fight(self, world, attack, defend, old_x, new_x):
        pass

    def draw_pos(self, world):
        n = world.get_n()
        m = world.get_m()
        x = random.randint(0, (n * m) - 1)
        if world.get_map()[x] == 0:
            return x
        else:
            return self.draw_pos(world)

    def set_strength(self, strength):
        self.__strength = strength

    def set_initiative(self, initiative):
        self.__initiative = initiative

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def set_age(self, age):
        self.__age = age

    def set_alive(self, alive):
        self.__alive = alive

    def set_xx(self, x, world):
        self.__pos_x = x
        world.add_to_map(self, x)

    def set_x(self, x, world, old_x):
        self.set_xx(x, world)
        world.add_to_map(0, old_x)

    def set_image(self, image):
        self.__image = image

    def get_strength(self):
        return self.__strength

    def get_initiative(self):
        return self.__initiative

    def get_symbol(self):
        return self.__symbol

    def get_age(self):
        return self.__age

    def get_alive(self):
        return self.__alive

    def get_x(self):
        return self.__pos_x

    def get_image(self):
        return self.__image

    def kill(self, world, to_kill):
        world.get_map()[to_kill.get_x()] = 0  # clearing map
        to_kill.set_alive(False)

    def from_file(self, power, age):
        self.set_age(age)
        self.set_strength(power)