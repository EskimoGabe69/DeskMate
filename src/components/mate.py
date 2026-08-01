import pygame
import core.constants as constants


class Mate(pygame.sprite.Sprite):
    """
    Class component which controls the logic regarding the mate.

    Usecase:
        mate = Mate(spritesheet, animation_coords)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(mate)
        all_sprites.draw()

    Attributes:
        spritesheet: which is gonna give the provided sprite for the mate
        animation_coords: which is a list with tuples that contain coordinations of the animation, such as(x_coordinate, y_coordinate, width, height)
    """

    def __init__(self, spritesheet, animation_coords, frame_duration=2) -> None:
        super().__init__()
        self.spritesheet = spritesheet
        self.animation = self.spritesheet.get_animation(
            animation_coords, frame_duration
        )
        self.original_image = self.animation["frames"][0]
        self.flipped_image = pygame.transform.flip(self.original_image, True, False) 
        self.image = self.original_image 
        self.rect = self.image.get_rect() 
        self.rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
        self.vx = 2
        self.facing_left = False

    def update(self) -> None:
        current_frame = self.spritesheet.update_animation(self.animation) 
        if current_frame is not None and current_frame != self.original_image:
            self.original_image = current_frame
            self.flipped_image = pygame.transform.flip(self.original_image, True, False)
        self.rect.x += self.vx
        if self.rect.right > constants.WIDTH or self.rect.left < 0:
            self.vx *= -1
            self.facing_left = not self.facing_left
        self.image = self.flipped_image if self.facing_left else self.original_image
