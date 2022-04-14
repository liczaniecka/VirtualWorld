from animal import Animal
import pygame
from pygame.locals import *
MAX = 10
STOP = 5


class Human(Animal):

    __cooldown = 0

    def __init__(self, world):
        x = self.draw_pos(world)
        self.set_alive(True)
        self.set_strength(5)
        self.set_initiative(4)
        self.set_symbol('H')
        self.set_xx(x, world)
        self.set_age(0)
        self.set_image(pygame.image.load(r'human.png'))

    def set_cooldown(self, stage):
        self.__cooldown = stage

    def get_cooldown(self):
        return self.__cooldown

    def action(self, world):
        x = self.get_x()
        n = world.get_n()
        m = world.get_m()
        run = True
        pygame.event.clear()
        while x == self.get_x():
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    x += 1
                if event.key == pygame.K_UP:
                    if x - n >= 0:
                        self.collision(world, x - n)
                if event.key == pygame.K_RIGHT:
                    if x % n != n - 1:
                        self.collision(world, x + 1)
                if event.key == pygame.K_DOWN:
                    if x + n < n * m:
                        self.collision(world, x + n)
                if event.key == pygame.K_LEFT:
                    if x % n != 0:
                        self.collision(world, x - 1)
                if event.key == pygame.K_SPACE:
                    if self.get_cooldown() == 0:
                        self.set_cooldown(MAX)
                        self.skill(world)
                        world.display_org()
                if event.key == pygame.K_s:
                    world.save_game()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                if mx < 900:
                    world.click_org(mx, my)
        if self.get_cooldown() > 0:
            if self.get_cooldown() >= STOP:
                self.skill(world)
            self.set_cooldown(self.get_cooldown() - 1)
        if not run:
            return False
        else:
            return True

    def skill(self, world):
        w_map = world.get_map()
        n = world.get_n()
        m = world.get_m()
        pos = self.get_x()
        text = ""
        if pos - n > 0 and w_map[pos - n] != 0:
            text += w_map[pos - n].get_symbol() + " gets killed by H"
            world.add_to_com(text)
            text = ""
            self.kill(world, w_map[pos - n])
        if (pos + 1) % n != n - 1 and w_map[pos + 1] != 0:
            text += w_map[pos + 1].get_symbol() + " gets killed by H"
            world.add_to_com(text)
            text = ""
            self.kill(world, w_map[pos + 1])
        if pos + n < n * m and w_map[pos + n] != 0:
            text += w_map[pos + n].get_symbol() + " gets killed by H"
            world.add_to_com(text)
            text = ""
            self.kill(world, w_map[pos + n])
        if (pos - 1) % n != 0 and w_map[pos - 1] != 0:
            text += w_map[pos - 1].get_symbol() + " gets killed by H"
            world.add_to_com(text)
            text = ""
            self.kill(world, w_map[pos - 1])
