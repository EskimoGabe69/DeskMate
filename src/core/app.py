import asyncio
import pygame

def run() -> None:
    pygame.display.set_caption("Something")
    asyncio.run(game_loop())


async def game_loop() -> None:
    pass
