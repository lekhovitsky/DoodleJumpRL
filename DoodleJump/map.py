from typing import Tuple
from pygame.sprite import Group
from DoodleJump.objects import *


class Map:
    camera: int
    objects: Group
    resolution: Tuple[int, int]

    def __init__(self, resolution: Tuple[int, int]):
        self.resolution = resolution

    def update(self):
        pass

    def reset(self):
        pass
