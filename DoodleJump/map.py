from typing import Tuple
from pygame.sprite import Group
from .objects import *


class Map:
    camera: int
    objects: Group
    resolution: Tuple[int, int]

    def __init__(self, resolution: Tuple[int, int]):
        self.resolution = resolution
        self.reset()

    def update(self):
        pass

    def reset(self):
        self.objects = Group()
