from typing import Tuple
import pygame


class Doodle(pygame.sprite.Sprite):
    image: str
    location: Tuple[float, float]
    velocity: Tuple[float, float]
    acceleration: Tuple[float, float]

    images = {
        'left_up': pygame.image.load('../assets/left_up.png'),
        'left_down': pygame.image.load('../assets/left_down.png'),
        'right_up': pygame.image.load('../assets/right_up.png'),
        'right_down': pygame.image.load('../assets/right_down.png')
    }

    def __init__(self, location: Tuple[float, float]):
        super().__init__()
        self.surf = self.images['right_down']
        self.rect = self.surf.get_rect(
            center=location
        )

    def update(self, action: int = 0):
        assert action in {0, 1, 2}

        if action:
            pass
