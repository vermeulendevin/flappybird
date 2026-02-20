import pygame
import constants as const

class Ground:
    def __init__(self):
        self.height = 100
        self.x1 = 0
        self.x2 = const.SCREEN_WIDTH
        self.speed = 3

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 <= -const.SCREEN_WIDTH:
            self.x1 = self.x2 + const.SCREEN_WIDTH
        if self.x2 <= -const.SCREEN_WIDTH:
            self.x2 = self.x1 + const.SCREEN_WIDTH

    def draw(self, screen):
        ground_y = const.SCREEN_HEIGHT - self.height
        pygame.draw.rect(screen, const.DARK_GREEN, (self.x1, ground_y, const.SCREEN_WIDTH, self.height))
        pygame.draw.rect(screen, const.DARK_GREEN, (self.x2, ground_y, const.SCREEN_WIDTH, self.height))