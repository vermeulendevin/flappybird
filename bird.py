import pygame
import constants as const

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.radius = 20

    def jump(self):
        self.velocity = -10

    def update(self):
        self.velocity += 0.5
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, const.YELLOW, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, ground_height):
        if self.y + self.radius >= const.SCREEN_HEIGHT - ground_height:
            return True
        if self.y - self.radius <= 0:
            return True
        return False