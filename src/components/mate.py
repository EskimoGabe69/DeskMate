import pygame
import core.constants as constants
import os

game_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(game_directory, ".."))
asset_directory = os.path.join(parent_directory, "assets")
image_file = pygame.image.load(os.path.join(asset_directory, "Doggo.png")).convert_alpha()

# NOTE: The sprite needs to be moved to main I think

class Mate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.image.blit(image_file, (0, 0))
        self.rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > constants.WIDTH or self.rect.left < 0:
            self.vx *= -1
