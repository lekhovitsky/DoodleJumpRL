import abc
import os.path

import pygame
from pygame.sprite import Sprite
from ..doodle import Doodle

ASSETS_DIR = os.path.join(
    os.path.dirname(__file__), '../assets')


class Platform(Sprite, abc.ABC):
    pass


class BasicPlatform(Platform):
    image = pygame.image.load(os.path.join(ASSETS_DIR, "green_platform.png"))

    def interact(self, doodle: Doodle):
        pass


class MovingPlatform(Platform):
    image = pygame.image.load(os.path.join(ASSETS_DIR, "blue_platform.png"))

    velocity: float

    def __init__(self, velocity: float):
        super().__init__()
        self.velocity = velocity

    def interact(self, doodle: Doodle):
        pass

    def update(self):
        pass


class BreakingPlatform(Platform):
    images = {
        'normal': pygame.image.load(os.path.join(ASSETS_DIR, "red_platform.png")),
        'broken': pygame.image.load(os.path.join(ASSETS_DIR, "red_platform_broken.png"))
    }
    broken: bool

    def __init__(self):
        super().__init__()
        self.broken = False

    def interact(self, doodle: Doodle):
        pass
