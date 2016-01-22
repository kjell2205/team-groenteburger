import pygame
from pygame.locals import *
import pygame
import sys

pygame.init()
pencere = pygame.display.set_mode((800, 800), pygame.SWSURFACE)
pygame.display.set_caption('Buy A Ride')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
sys.exit()
pygame.display.flip()


class Node:
    def __init__(self, value, tail):
        self.Tail = tail
        self.Value = value
        self.IsEmpty = False


class Empty:
    def __init__(self):
        self.IsEmpty = True


Empty = Empty()


class Tegel:
    def __init__(self, ID, Positie, Playerlist,
                 Plaatje):  # als je deze methode aanroept in de vorm van Tegel(positie, playerlist, plaatje) en het resultaat
        self.ID = ID  # in een variabele stopt dan krijg je een tegel terug
        self.Positie = Positie  # met daarin de positie als eerste argument de lijst met players als tweede argument en het plaatje als derde
        self.Playerlist = Playerlist
        self.Plaatje = Plaatje

    def Update(self):
        # doe iets hier

        return self

# dan maken we een lijst van tegels met een aantal spelers op de eerste tegel

tegellijst = Node(Tegel(0, (0, 0), Empty(), "geenplaatje"), Empty())


class Speler:
    def __init__(self, ID, positie, geld, kleur):
        self.ID = ID
        self.Positie = positie
        self.Geld = geld
        self.Kleur = kleur
        self.car_texture = pygame.image.load(os.path.join("Content", "Board.png")).convert()

    def newposition(self):
        # doe iets

        return

    def move(self):

        # todo

    def gooidobbelsteen(self):
        # todo


class Card:
    def __init__(self, positie, nummer):
        self.Positie = positie
        self.Nummer = nummer
        self.car_texture = pygame.image.load(os.path.join("Content", "Board.png")).convert()


def Draw(self, screen):

