import pygame
import core.constants as constants


class Mate(pygame.sprite.Sprite):
    def __init__(self, mate_image) -> None:
        super().__init__()
        self.mate_image = mate_image
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.image.blit(self.mate_image, (0, 0))
        self.rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > constants.WIDTH or self.rect.left < 0:
            self.vx *= -1
