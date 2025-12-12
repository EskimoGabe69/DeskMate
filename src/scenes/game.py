import core.input as input
from scenes.scene import Scene
import scenes.menu


class Game(Scene):
    def enter(self) -> None:
        pass

    def execute(self, mouse_buffer: input.InputBuffer) -> None:
        if mouse_buffer[input.MouseButton.LEFT] == input.InputState.PRESSED:
            self.statemachine.change_state(scenes.menu.menu)
            return

    def exit(self) -> None:
        pass
