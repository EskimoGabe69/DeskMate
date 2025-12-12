from abc import abstractmethod
import pygame

from components.statemachine import State
import core.input as input


class Scene(State):
    @abstractmethod
    def enter(self) -> None:
        pass

    @abstractmethod
    def execute(
        self, surface: pygame.Surface, dt: float, mouse_buffer: input.InputBuffer
    ) -> None:
        pass

    @abstractmethod
    def exit(self) -> None:
        pass
