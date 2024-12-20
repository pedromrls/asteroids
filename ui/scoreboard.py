import pygame  # type: ignore
from utils.constants import *

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.color = FONT_COLOR_RGB
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.position = SCORE_POS

    def draw(self, screen):
        render = self.font.render(f"SCORE: {self.score:,}", False,self.color)
        screen.blit(render, self.position)

    def add_points(self, points):
        self.score += points