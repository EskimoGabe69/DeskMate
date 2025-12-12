from screeninfo import get_monitors
# monitors
monitors = get_monitors()
monitor = monitors[0]
# NOTE: Later changing this to just user screen size or manual
# Settings 
WIDTH = 640
HEIGHT = 360
FPS = 30
CAPTION = "Desk mate"
WINDOW_SIZE = (WIDTH, HEIGHT)
CENTRE = (WIDTH // 2, HEIGHT // 2)
SCREEN_WIDTH = monitor.width
SCREEN_HEIGHT = monitor.height
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WINDOW_SETUP = {
    "size": WINDOW_SIZE,
}

SCREEN_SETUP = {
    "size": SCREEN_SIZE,
}
# Colors 
BLACK = (0,0,0)


