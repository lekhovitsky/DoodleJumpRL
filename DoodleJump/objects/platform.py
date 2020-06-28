import abc
from pygame.sprite import Sprite
from ..doodle import Doodle


class Platform(Sprite, abc.ABC):
    pass


class BasicPlatform(Platform):

    def interact(self, doodle: Doodle):
        pass


class MovingPlatform(Platform):
    velocity: float

    def __init__(self, velocity: float):
        super().__init__()
        self.velocity = velocity

    def interact(self, doodle: Doodle):
        pass

    def update(self):
        pass


class BreakingPlatform(Platform):
    broken: bool

    def __init__(self):
        super().__init__()
        self.broken = False

    def interact(self, doodle: Doodle):
        pass
