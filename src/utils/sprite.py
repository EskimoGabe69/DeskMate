import pygame
from core.constants import WHITE

class SpriteSheet:
    def __init__(self, file) -> None:
        self.sheet = pygame.image.load(file)

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(WHITE)
        return sprite
