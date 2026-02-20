from screeninfo import get_monitors
import pygame

monitors = get_monitors()
first_monitor = monitors[0]

WIDTH = first_monitor.width
HEIGHT = first_monitor.height
WINDOW_SIZE = (WIDTH, HEIGHT)
WINDOW_CENTRE = (WIDTH // 2, HEIGHT // 2)
WINDOW_SETUP = {"size": WINDOW_SIZE, "depth": 0, "display": 0, "vsync": 0}
FPS = 30
CAPTION = "Deskmate by EskimoGabe"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN = pygame.surface.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
TRANSPARENT = (255, 255, 255, 0)
