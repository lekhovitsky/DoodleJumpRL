import os.path
from typing import Tuple
import pygame

ASSETS_DIR = os.path.join(
    os.path.dirname(__file__), 'assets')


class Doodle(pygame.sprite.Sprite):
    image: str
    location: Tuple[float, float]
    velocity: Tuple[float, float]
    acceleration: Tuple[float, float]

    images = {
        'left_up': pygame.image.load(os.path.join(ASSETS_DIR, 'left_up.png')),
        'left_down': pygame.image.load(os.path.join(ASSETS_DIR, 'left_down.png')),
        'right_up': pygame.image.load(os.path.join(ASSETS_DIR, 'right_up.png')),
        'right_down': pygame.image.load(os.path.join(ASSETS_DIR, 'right_down.png'))
    }

    def __init__(self, location: Tuple[float, float]):
        super().__init__()
        self.location = location
        self.surf = self.images['right_down']
        self.rect = self.surf.get_rect(
            center=location
        )

    def update(self, action: int = 0):
        assert action in {0, 1, 2}

        if action:
            pass
