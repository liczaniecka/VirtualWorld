from animal import Animal
from antelope import Antelope
from belladona import Belladona
from csheep import Csheep
from fox import Fox
from grass import Grass
from guarana import Guarana
from hogweed import Hogweed
from human import Human
from organism import Organism
from plant import Plant
from sheep import Sheep
from thistle import Thistle
from turtle import Turtle
from wolf import Wolf
import pygame
from pygame.locals import *
pygame.font.init()


WIDTH, HEIGHT, WIDTH2 = 900, 900, 1200
GREEN = (38, 175, 21)
BLACK = (56, 89, 36)
WHITE = (255, 255, 255)
WIN = pygame.display.set_mode((WIDTH2, HEIGHT))
BCKG = pygame.Rect(WIDTH2 - 300, 0, 300, HEIGHT)
FONT = pygame.font.SysFont('arial', 20)
FONT2 = pygame.font.SysFont('arial', 60)
pygame.display.set_caption("Virtual world - Lilianna Czaniecka 184613 DE")

class World:
    __n = 0
    __m = 0
    __map = []
    __org = []
    __commentator = []
    __a = 0
    __p = 0


    def __init__(self, n, m):
        self.__n = int(n)
        self.__m = int(m)
        self.__map = [0] * (int(m) * int(n))

    def get_map(self):
        return self.__map

    def get_org(self):
        return self.__org

    def get_com(self):
        return self.__commentator

    def add_to_com(self, text):
        self.__commentator.append(text)

    def set_a(self, a):
        self.__a = a

    def set_p(self, p):
        self.__p = p

    def get_n(self):
        return self.__n

    def get_m(self):
        return self.__m

    def add_to_org(self, organism):
        if len(self.__org) == 0:
            self.__org.append(organism)
        else:
            i = 0
            while i < len(self.__org) and self.__org[i].get_initiative() >= organism.get_initiative():
                i += 1

            self.__org.insert(i, organism)

    def create_world(self):
        organism = Human(self)
        self.add_to_org(organism)
        for i in range(self.__a):
            organism = Antelope(self, 0, False)
            self.add_to_org(organism)
            organism = Fox(self, 0, False)
            self.add_to_org(organism)
            organism = Sheep(self, 0, False)
            self.add_to_org(organism)
            organism = Turtle(self, 0, False)
            self.add_to_org(organism)
            organism = Wolf(self, 0, False)
            self.add_to_org(organism)
            organism = Csheep(self, 0, False)
            self.add_to_org(organism)
        for i in range(self.__p):
            organism = Belladona(self, 0, False)
            self.add_to_org(organism)
            organism = Grass(self, 0, False)
            self.add_to_org(organism)
            organism = Guarana(self, 0, False)
            self.add_to_org(organism)
            organism = Hogweed(self, 0, False)
            self.add_to_org(organism)
            organism = Thistle(self, 0, False)
            self.add_to_org(organism)

    def display_org(self):
        img_h = HEIGHT // (self.get_m())
        img_w = WIDTH // (self.get_n())
        for i in range(len(self.__org)):
            if self.__org[i].get_alive():
                WIN.blit(pygame.transform.scale(self.__org[i].get_image(), (img_w, img_h)), ((self.__org[i].get_x() % self.__n)*img_w, (self.__org[i].get_x() // self.__n)*img_h))
        pygame.display.update()

    def display_commentator(self):
        WIN.fill(GREEN)
        pygame.draw.rect(WIN, BLACK, BCKG)
        y = 10
        if len(self.__commentator) > 29:
            x = len(self.__commentator)
            r = x - 29
            for i in range(r):
                del self.__commentator[i]
        if len(self.__commentator) <= 29:
            for i in range(len(self.__commentator)):
                text = self.__commentator[i]
                text = FONT.render(str(text), True, WHITE)
                WIN.blit(text, (WIDTH2 - 290, y))
                y += 30

    def make_turn(self, alive):
        g_quit = True
        while alive:
            alive = False
            for specie in self.get_org():
                if specie.get_symbol() == 'H' and specie.get_alive():
                    self.display_commentator()
                    self.display_org()
                    alive = True
                if specie.get_alive():
                    if specie.get_symbol() == 'H':
                        g_quit = specie.action(self)
                    else:
                        specie.action(self)
                if not g_quit:
                    alive = g_quit
                specie.set_age(specie.get_age() + 1)
            for i in range(0, len(self.get_org()))[::-1]:
                if not self.get_org()[i].get_alive():
                    del self.get_org()[i]

    def add_to_map(self, organism, x):
        self.__map[int(x)] = organism

    def start_game(self):
        move = False
        dimensions = ""
        text_in = ""
        orgs = ""
        while not move:
            WIN.fill(GREEN)
            text = "Welcome to the virtual world!"
            text = FONT2.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 100))
            text = "Arrow keys to move human"
            text = FONT.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 180))
            text = "Space to start special skill"
            text = FONT.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 230))
            text = "Escape to end game"
            text = FONT.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 280))
            text = "S to save the state of game"
            text = FONT.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 330))
            text = "Left click to add new organism"
            text = FONT.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 380))
            text = "Please, decide game mode"
            text = FONT2.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 430))
            text = "create game"
            text = FONT2.render(str(text), True, BLACK)
            cre_game = WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 530))
            text = "upload game"
            text = FONT2.render(str(text), True, BLACK)
            up_game = WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 630))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if up_game.collidepoint(mx, my):
                        self.upload_game()
                        return
                    elif cre_game.collidepoint(mx, my):
                        move = True
        move = False
        while not move:
            WIN.fill(GREEN)
            text = "Please, type in the size of the map"
            text = FONT2.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 300))
            text = "(two ints, space between)"
            text = FONT2.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 400))
            text_in = FONT2.render(str(dimensions), True, BLACK)
            WIN.blit(text_in, (WIDTH2//2 - text_in.get_width()//2, 500))
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        dimensions = dimensions[:-1]
                    elif event.key == pygame.K_RETURN:
                        pygame.event.clear()
                        move = True
                    else:
                        dimensions += event.unicode
        xx = dimensions.split(" ")
        self.__n = int(xx[0])
        self.__m = int(xx[1])
        self.__map = [0] * (int(self.__m) * int(self.__n))
        move = False
        while not move:
            WIN.fill(GREEN)
            text = "Please, chose number of organisms of each specie"
            text = FONT2.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 300))
            text = "(two ints, space between [animals, plants])"
            text = FONT2.render(str(text), True, BLACK)
            WIN.blit(text, (WIDTH2//2 - text.get_width()//2, 400))
            text_in = FONT2.render(str(orgs), True, BLACK)
            WIN.blit(text_in, (WIDTH2//2 - text_in.get_width()//2, 500))
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        orgs = orgs[:-1]
                    elif event.key == pygame.K_RETURN:
                        pygame.event.clear()
                        move = True
                    else:
                        orgs += event.unicode
        yy = orgs.split(" ")
        self.__a = int(yy[0])
        self.__p = int(yy[1])
        self.create_world()
        self.make_turn(True)

    def upload_game(self):
        f = open("game.txt", "r")
        for line in f:
            x = line.split(" ")
            if len(line) == 2:
                self.__n = int(x[0])
                self.__m = int(x[1])
                self.__map = [0] * (int(self.__m) * int(self.__n))
            else:
                if x[0] == "A":
                    n = Antelope(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "C":
                    n = Csheep(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "F":
                    n = Fox(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "S":
                    n = Sheep(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "T":
                    n = Turtle(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "W":
                    n = Wolf(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "!":
                    n = Belladona(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "#":
                    n = Grass(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "+":
                    n = Guarana(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "*":
                    n = Hogweed(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "%":
                    n = Thistle(self, int(x[1]), True)
                    n.from_file(int(x[2]), int(x[3]))
                    self.add_to_org(n)
                elif x[0] == "H":
                    n = Human(self)
                    n.from_file(int(x[2]), int(x[3]))
                    n.set_xx(int(x[1]), self)
                    n.set_cooldown(int(x[4]))
                    self.add_to_org(n)
        self.make_turn(True)
        f.close()

    def save_game(self):
        f = open("game.txt", "w")
        text = str(self.get_n()) + " " + str(self.get_m()) + "\n"
        f.write(text)
        for specie in self.get_org():
            if specie.get_alive:
                if specie.get_symbol() != "H":
                    s_text = specie.get_symbol() + " " + str(specie.get_x()) + " " + str(specie.get_strength()) + " " + str(specie.get_age()) + "\n"
                    f.write(s_text)
                else:
                    s_text = specie.get_symbol() + " " + str(specie.get_x()) + " " + str(specie.get_strength()) + " " + str(specie.get_age()) + " " + str(specie.get_cooldown()) + "\n"
                    f.write(s_text)
        f.close()

    def click_org(self, mx, my):
        pygame.display.update()
        pygame.draw.rect(WIN, BLACK, BCKG)
        img_h = HEIGHT // (self.get_m())
        img_w = WIDTH // (self.get_n())
        x = mx//img_w
        y = my//img_h
        i = self.__n * y + x
        if self.__map[i] == 0:
            chosen = False
            pos = 10
            text = "Antelope"
            text = FONT.render(str(text), True, WHITE)
            o_antelope = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Belladona"
            text = FONT.render(str(text), True, WHITE)
            o_belladona = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Cyber Sheep"
            text = FONT.render(str(text), True, WHITE)
            o_csheep = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Fox"
            text = FONT.render(str(text), True, WHITE)
            o_fox = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Grass"
            text = FONT.render(str(text), True, WHITE)
            o_grass = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Guarana"
            text = FONT.render(str(text), True, WHITE)
            o_guarana = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Hogweed"
            text = FONT.render(str(text), True, WHITE)
            o_hogweed = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Sheep"
            text = FONT.render(str(text), True, WHITE)
            o_sheep = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Thistle"
            text = FONT.render(str(text), True, WHITE)
            o_thistle = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Turtle"
            text = FONT.render(str(text), True, WHITE)
            o_turtle = WIN.blit(text, (WIDTH2 - 290, pos))
            pos += 40
            text = "Wolf"
            text = FONT.render(str(text), True, WHITE)
            o_wolf = WIN.blit(text, (WIDTH2 - 290, pos))
            while not chosen:
                ev = pygame.event.wait()
                if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                    mx2, my2 = pygame.mouse.get_pos()
                    if o_antelope.collidepoint(mx2, my2):
                        o = Antelope(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_belladona.collidepoint(mx2, my2):
                        o = Belladona(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_csheep.collidepoint(mx2, my2):
                        o = Csheep(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_fox.collidepoint(mx2, my2):
                        o = Fox(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_grass.collidepoint(mx2, my2):
                        o = Grass(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_guarana.collidepoint(mx2, my2):
                        o = Guarana(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_hogweed.collidepoint(mx2, my2):
                        o = Hogweed(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_sheep.collidepoint(mx2, my2):
                        o = Sheep(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_thistle.collidepoint(mx2, my2):
                        o = Thistle(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_turtle.collidepoint(mx2, my2):
                        o = Turtle(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                    elif o_wolf.collidepoint(mx2, my2):
                        o = Wolf(self, i, True)
                        self.add_to_org(o)
                        chosen = True
                self.display_org()
        else:
            text = "Please, choose empty field"
            text = FONT.render(str(text), True, WHITE)
            WIN.blit(text, (WIDTH2 - 290, 10))

        pygame.display.update()
