import abc
from pygame.sprite import Sprite


class Platform(Sprite, abc.ABC):
    pass


class BasicPlatform(Platform):
    pass


class MovingPlatform(Platform):
    velocity: float

    def __init__(self, velocity: float):
        super().__init__()
        self.velocity = velocity

    def update(self):
        pass


class BreakingPlatform(Platform):
    broken: bool

    def __init__(self):
        super().__init__()
        self.broken = False
