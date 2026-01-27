import pygame
import sys

# constants
WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()


class Mate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vx = 2

    def update(self) -> None:
        self.rect.x += self.vx
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vx *= -1


all_sprites = pygame.sprite.Group()
mate = Mate()
all_sprites.add(mate)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deskmate made by EskimoGabe")
clock = pygame.time.Clock()
if __name__ == "__main__":
    while True:
        all_sprites.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill(BLACK)
        all_sprites.draw(window)
        pygame.display.flip()
