import pygame
from core.constants import WHITE


class SpriteSheet:
    """
    Utility to handle spritesheets and the spritesheet animation.

    Attributes:
        file: A LiteralString. Preferly use the OS library, example: os.path.join(os.path.dirname(__file__), filename.file)

    Use case:
        spritesheet = SpriteSheet(path_of_the_spritesheet)
    """

    def __init__(self, file) -> None:
        self.sheet = pygame.image.load(file)

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(WHITE)
        return sprite

    def get_animation(self, coords, frame_duration):
        frames = [self.get_sprite(x, y, w, h) for (x, y, w, h) in coords]
        return {
            "frames": frames,
            "current_frame": 0,
            "frame_counter": 0,
            "frame_duration": frame_duration,
        }

    def update_animation(self, animation):
        animation["frame_counter"] += 1
        if animation["frame_counter"] >= animation["frame_duration"]:
            animation["frame_counter"] = 0
            animation["current_frame"] = (animation["current_frame"] + 1) % len(
                animation["frames"]
            )
            return animation["frames"][animation["current_frame"]]
