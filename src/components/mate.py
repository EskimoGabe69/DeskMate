import pygame
import core.constants as constants


class Mate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((constants.RED))
        self.rect = self.image.get_rect()
        self.rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > constants.WIDTH or self.rect.left < 0:
            self.vx *= -1

