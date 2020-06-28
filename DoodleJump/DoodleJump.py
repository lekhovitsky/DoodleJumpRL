import pygame
from pygame.sprite import Group
from .objects import Doodle, Spring, Platform


class DoodleJump:
    score: int

    def __init__(self):
        self.score = 0

    def play(self, action):
        pass

    def render(self):
        pass

    def get_screen(self):
        pass

    @staticmethod
    def play_game():
        game = DoodleJump()

        while True:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                action = 1
            elif key[pygame.K_RIGHT]:
                action = 2
            else:
                action = 0

            game.play(action)
            game.render()

            if any([e.type == pygame.QUIT for e in pygame.event.get()]):
                break

        print(f"Final score = {game.score}")


if __name__ == "__main__":
    DoodleJump.play_game()
