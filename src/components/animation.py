import pygame
import core.constants as const  # NOTE: this works

class AnimationMate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (const.SCREEN_WIDTH // 2, const.SCREEN_HEIGHT // 2)
        self.vx = 3

    def update(self):
        self.rect.x += self.vx
        if self.rect.x <= 0:
            self.vx = -self.vx
            self.rect.x = 0
        elif self.rect.x >= const.SCREEN_WIDTH - self.rect.width:
            self.vx = -self.vx
            self.rect.x = const.SCREEN_WIDTH - self.rect.width
