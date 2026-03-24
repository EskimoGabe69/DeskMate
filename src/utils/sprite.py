import pygame

def get_sprite(posx, posy, width, height, sprite_sheet):
    """Extracts image from sprite sheet"""
    image = pygame.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    image.set_colorkey("BLACK")

    return image
