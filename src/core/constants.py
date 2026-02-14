from screeninfo import get_monitors
import pygame

monitors = get_monitors()
first_monitor = monitors[0]

WIDTH = first_monitor.width
HEIGHT = first_monitor.height
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN = pygame.surface.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
TRANSPARENT = (255, 255, 255, 0)

