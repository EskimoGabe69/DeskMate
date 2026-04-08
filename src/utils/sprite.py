import pygame
from core.constants import BLACK


# # NOTE: Maybe read the docs about the sprite slicer
# def get_sprite(posx, posy, width, height, sprite_sheet):
#     """Extracts image from sprite sheet"""
#     image = pygame.Surface([width, height])
#     image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
#     image.set_colorkey("BLACK")


#     return image
class SpriteSheet:
    def __init__(self, file) -> None:
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite
