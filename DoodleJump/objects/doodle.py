from typing import Tuple
from pygame.sprite import Sprite


class Doodle(Sprite):
    velocity: Tuple[float, float]
    acceleration: Tuple[float, float]
    pass
