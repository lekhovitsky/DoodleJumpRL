import os.path

import pygame
from pygame.sprite import Sprite

from ..doodle import Doodle
from .platform import Platform

ASSETS_DIR = os.path.join(
    os.path.dirname(__file__), '../assets')


class Spring(Sprite):
    images = {
        'coiled': pygame.image.load(os.path.join(ASSETS_DIR, "spring_coiled.png")),
        'loose': pygame.image.load(os.path.join(ASSETS_DIR, "spring_loose.png"))
    }

    platform: Platform
    coiled: bool

    def __init__(self, platform: Platform):
        super().__init__()
        self.platform = platform
        self.coiled = True

    def interact(self, doodle: Doodle):
        pass
