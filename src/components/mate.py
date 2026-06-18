import pygame
import core.constants as constants

class Mate(pygame.sprite.Sprite):
    def __init__(self, spritesheet, animation_coords, frame_duration=2) -> None:
        super().__init__()
        self.spritesheet = spritesheet
        self.animation = self.spritesheet.get_animation(animation_coords, frame_duration)
        self.mate_image = self.animation["frames"][0]
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.blit(self.mate_image, (0, 0))
        self.rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.image = self.spritesheet.update_animation(self.animation)
        self.rect.x += self.vx
        if self.rect.right > constants.WIDTH or self.rect.left < 0:
            self.vx *= -1
            self.image = pygame.transform.flip(self.image, True, False)
