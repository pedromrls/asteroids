import pygame  # type: ignore

class Scoreboard:
    def __init__(self, x, y, font_size):
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.x = x
        self.y = y
        pass

    def draw(self, screen):
        render = self.font.render(str(self.score), False,(255, 255, 255) )
        screen.blit(render, (self.x, self.y))

    def update(self):
        pass

    def add_points(self, points):
        self.score += points