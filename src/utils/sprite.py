import pygame
from core.constants import WHITE

class SpriteSheet:
    def __init__(self, file) -> None:
        self.sheet = pygame.image.load(file)

# NOTE: gonna change location for x and y coords and have width and height pre-assigned
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(WHITE)
        return sprite


# NOTE: Gonna add animation here
    # def get_animation(self, coords, frame_duration):
    #     frames = [self.get_sprite(frame, )]
