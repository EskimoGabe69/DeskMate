import pygame


class CharacterAnimatedFrames:
    def __init__(self, filename, tag, suffix, frames) -> None:
        self.frames = []
        for i in range(frames):
            self.frames.append(
                pygame.image.load(filename + tag + str(i) + "." + suffix).convert()
            )
