from typing import Tuple

import pygame

from .map import Map
from .doodle import Doodle


class DoodleJump:
    RESOLUTION: Tuple[int, int] = (800, 600)

    score: int

    map: Map
    doodle: Doodle

    def __init__(self):
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.map = Map(self.RESOLUTION)
        self.reset()

    def reset(self):
        self.score = 0
        self.map.reset()
        self.doodle = Doodle((380, 350))

    def update(self, action: int = 0):
        assert action in {0, 1, 2}

        self.doodle.update(action)
        self.map.update()

        if obj := pygame.sprite.spritecollideany(self.doodle, self.map.objects):
            obj.interact(self.doodle)

    def render(self):
        pass

    def get_screen(self):
        pass

    @staticmethod
    def play_game():
        game = DoodleJump()

        running = True
        while running:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                action = 1
            elif key[pygame.K_RIGHT]:
                action = 2
            else:
                action = 0

            game.update(action)
            game.render()

            if any([e.type == pygame.QUIT for e in pygame.event.get()]):
                running = False

        print(f"Final score = {game.score}")


if __name__ == "__main__":
    DoodleJump.play_game()
