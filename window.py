from world import World
import pygame
WIDTH, HEIGHT = 900, 500
GREEN = (38, 175, 21)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Window:

    WIN.fill(GREEN)
    def display_animals(self, world):
        img_h = HEIGHT//(world.get_m())
        img_w = WIDTH//(world.get_n())

        for specie in world.get_org():
            if specie.get_alive():
                WIN.blit(specie.get_image(), (img_h, img_w))
        pygame.update()