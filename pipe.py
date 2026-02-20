import pygame
import constants as const
import random

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 70
        self.gap = 200
        self.top_height = random.randint(100, 300)
        self.speed = 3
        self.passed = False

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, const.GREEN, (self.x, 0, self.width, self.top_height))
        bottom_y = self.top_height + self.gap
        pygame.draw.rect(screen, const.GREEN, (self.x, bottom_y, self.width, const.SCREEN_HEIGHT - bottom_y))

    def is_off_screen(self):
        return self.x + self.width < 0

    def check_collision(self, bird):
        if bird.x + bird.radius > self.x and bird.x - bird.radius < self.x + self.width:
            if bird.y - bird.radius < self.top_height or bird.y + bird.radius > self.top_height + self.gap:
                return True
        return False

    def check_passed(self, bird):
        if not self.passed and bird.x > self.x + self.width:
            self.passed = True
            return True
        return False