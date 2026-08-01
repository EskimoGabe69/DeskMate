import pygame


class CharacterAnimatedFrames:
    """
    A component which turns animated frames into filenames loading corresponding images into the pygame image load method

    Attributes:
        filename (str): Base filename for the animation frames.
        tag (str): tag between the filenamed and frame number.
        suffix (str): file extension for frames(example: jpg and png)
        frames (int): Number of frames in animation sequence.
    """

    def __init__(self, filename, tag, suffix, frames) -> None:
        self.frames = []
        for i in range(frames):
            self.frames.append(
                pygame.image.load(filename + tag + str(i) + "." + suffix).convert()
            )
