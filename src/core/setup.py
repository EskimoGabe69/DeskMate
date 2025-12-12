import sys
import pygame
import platform
import core.constant as const

pygame.init()

if sys.platform == "emscripten": # For browser
    platform.window.canvas.style.imageRendering = "pixelated"
    screen = pygame.display.set_mode(const.SCREEN_SETUP["size"])
else:
    screen = pygame.display.set_mode(**const.SCREEN_SETUP)

clock = pygame.time.Clock()

print("Setup complete")
