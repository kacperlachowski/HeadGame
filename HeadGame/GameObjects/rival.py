from random import randrange
import pygame


class Rival:
    r = None
    g = None
    b = None
    movement = 5
    width = 0
    height = 30
    x = 0
    y = 0
    rival = None

    def __init__(self, window_width):
        self.r = randrange(256)
        self.g = randrange(256)
        self.b = randrange(256)
        self.width = (randrange(3) + 1) * 10
        self.x = (randrange(window_width - self.width - 1) + 1)
        self.rival = pygame.Rect(self.x, self.y, self.width, self.height)

    def gamer_on_bottom(self):
        self.rival.y += self.movement
        self.y += self.movement
