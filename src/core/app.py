import pygame
import asyncio
import core.constants as const
import core.setup as setup
import core.input as input
from components import animation
from components.statemachine import StateMachine
from scenes.menu import Menu


# NOTE: some of the stuff belongs to a different module
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_WIDTH))
sprite_collection = pygame.sprite.Group()
mate = animation.AnimationMate()
sprite_collection.add(mate)


# TODO: Add a state machine and scenes


def run() -> None:
    pygame.display.set_caption(const.CAPTION)
    # TODO: put an icon here per chance
    scene_manager = StateMachine(Menu)
    asyncio.run(game_loop(setup.screen,setup.clock, scene_manager))


async def game_loop(
    surface: pygame.Surface, clock: pygame.time.Clock, scene_manager: StateMachine
) -> None:

    mouse_buffer: input.InputBuffer = [
        input.InputState.NOTHING for _ in input.MouseButton
    ]

    print("Starting game loop")
    while True:
        elapsed_time = clock.tick(const.FPS)
        dt = elapsed_time / 1000.0
        running = input_event_queue()

        if not running:
            terminate(surface)

        update_mouse_buffer(mouse_buffer)
        scene_manager.execute(surface, dt, mouse_buffer)
        sprite_collection.update()
        screen.fill((0, 0, 0))
        sprite_collection.draw(screen)
        pygame.display.flip()
        await asyncio.sleep(0)


def input_event_queue() -> bool:
    """
    Pumps the event queue and handle application events
    Return: False if should terminate, else True
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True


def update_mouse_buffer(mouse_buffer: input.InputBuffer) -> None:
    mouse_pressed = pygame.mouse.get_pressed()  # doesnt work in the web
    for button in input.MouseButton:
        if mouse_pressed[button]:
            if (
                mouse_buffer[button] == input.InputState.NOTHING
                or mouse_buffer[button] == input.InputState.RELEASED
            ):
                mouse_buffer[button] = input.InputState.RELEASED
            elif mouse_buffer[button] == input.InputState.PRESSED:
                mouse_buffer[button] = input.InputState.HELD
        else:
            if (
                mouse_buffer[button] == input.InputState.PRESSED
                or mouse_buffer[button] == input.InputState.HELD
            ):
                mouse_buffer[button] = input.InputState.RELEASED
            elif mouse_buffer[button] == input.InputState.RELEASED:
                mouse_buffer[button] = input.InputState.NOTHING


def terminate(surface: pygame.Surface) -> None:
    print("Terminated application")
    surface.fill(const.BLACK)
    pygame.quit()
    raise SystemExit
