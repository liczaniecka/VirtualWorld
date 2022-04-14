from plant import Plant
import pygame
TRIALS = 3


class Thistle(Plant):

    def __init__(self, world, x, child):
        if not child:
            x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(0)
        self.set_initiative(0)
        self.set_symbol('%')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'thistle.png'))

    def spawn(self, world, x, child):
        return Thistle(world, x, child)

    def action(self, world):
        for i in range(TRIALS):
            self.reproduction(world)