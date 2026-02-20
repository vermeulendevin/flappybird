import pygame
import sys
import constants
from bird import Bird
from pipe import Pipe
from ground import Ground


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

        # Game state
        self.game_active = False
        self.score = 0
        self.running = True

        # Game objects
        self.bird = Bird()
        self.ground = Ground()
        self.pipes = []
        self.pipe_spawn_timer = 0

    def reset_game(self):
        self.game_active = True
        self.bird = Bird()
        self.pipes.clear()
        self.score = 0
        self.pipe_spawn_timer = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_active:
                        self.bird.jump()
                    else:
                        self.reset_game()

    def update(self):
        if self.game_active:
            self.bird.update()

            # Check ground/ceiling collision
            if self.bird.check_collision(self.ground.height):
                self.game_active = False

            self.ground.update()

            self.pipe_spawn_timer += 1
            if self.pipe_spawn_timer > 90:
                new_pipe = Pipe(constants.SCREEN_WIDTH)
                self.pipes.append(new_pipe)
                self.pipe_spawn_timer = 0

            for pipe in self.pipes[:]:
                pipe.update()

                # Check collision with bird
                if pipe.check_collision(self.bird):
                    self.game_active = False

                if pipe.check_passed(self.bird):
                    self.score += 1

                if pipe.is_off_screen():
                    self.pipes.remove(pipe)

    def draw(self):
        self.screen.fill(constants.SKY_BLUE)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.ground.draw(self.screen)

        self.bird.draw(self.screen)

        if self.game_active:
            font = pygame.font.Font(None, 50)
            score_text = font.render(str(self.score), True, constants.WHITE)
            self.screen.blit(score_text, (constants.SCREEN_WIDTH // 2 - 20, 50))
        else:
            font_large = pygame.font.Font(None, 60)
            font_small = pygame.font.Font(None, 30)

            if self.score == 0:
                title_text = font_large.render("Flappy Bird", True, constants.WHITE)
                self.screen.blit(title_text, (constants.SCREEN_WIDTH // 2 - 120, constants.SCREEN_HEIGHT // 2 - 50))
                start_text = font_small.render("Press SPACE to Start", True, constants.WHITE)
                self.screen.blit(start_text, (constants.SCREEN_WIDTH // 2 - 100, constants.SCREEN_HEIGHT // 2 + 20))
            else:
                game_over_text = font_large.render("Game Over!", True, constants.WHITE)
                self.screen.blit(game_over_text, (constants.SCREEN_WIDTH // 2 - 110, constants.SCREEN_HEIGHT // 2 - 50))
                score_text = font_small.render(f"Score: {self.score}", True, constants.WHITE)
                self.screen.blit(score_text, (constants.SCREEN_WIDTH // 2 - 50, constants.SCREEN_HEIGHT // 2))
                restart_text = font_small.render("Press SPACE to Restart", True, constants.WHITE)
                self.screen.blit(restart_text, (constants.SCREEN_WIDTH // 2 - 110, constants.SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(constants.FPS)

        pygame.quit()
        sys.exit()