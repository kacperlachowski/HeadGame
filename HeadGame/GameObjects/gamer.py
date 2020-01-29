import pygame


class Gamer:
    movement = 25
    width = 50
    height = 30
    x = None
    y = None
    player = None

    last_movement = -1

    def __init__(self, window_width, window_height):
        self.x = window_width/2 - 25
        self.y = window_height - 50
        self.player = pygame.Rect(self.x, self.y, self.width, self.height)

    def gamer_on_left(self):
        self.player.x -= self.movement
        self.x -= self.movement

    def gamer_on_right(self):
        self.player.x += self.movement
        self.x += self.movement
