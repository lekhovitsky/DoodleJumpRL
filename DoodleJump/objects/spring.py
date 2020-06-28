from pygame.sprite import Sprite
from ..doodle import Doodle
from .platform import Platform


class Spring(Sprite):
    platform: Platform
    coiled: bool

    def __init__(self, platform: Platform):
        super().__init__()
        self.platform = platform
        self.coiled = True

    def interact(self, doodle: Doodle):
        pass
