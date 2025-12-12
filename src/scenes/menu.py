import core.input as input
# from components.animation import AnimationMate

from scenes.scene import Scene
import scenes.game

# DEBUG = AnimationMate("spin", ) TODO: work on the spin thingy what it does

class Menu(Scene):
    def enter(self) -> None: pass

    def execute(self, mouse_buffer: input.InputBuffer) -> None:
        if (mouse_buffer[input.MouseButton.LEFT] == input.InputState.PRESSED):
            self.statemachine.change_state(scenes.game.game)
            return

    def exit(self) -> None: pass
