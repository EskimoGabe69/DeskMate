from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, statemachine: StateMachine) -> None:
        self.statemachine = statemachine

    @abstractmethod
    def enter(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def exit(self) -> None:
        pass


class StateMachine:
    def __init__(self, initial_state: State) -> None:
        self.next_state = None
        self.current_state = initial_state(self)
        self.current_state.enter()

    def execute(self, *args, **kwargs) -> None:
        self.current_state(*args, **kwargs)

        if self.next_state is not None:
            self.current_state.exit()
            self.current_state = self.next_state(self)
            self.next_state = None
            self.current_state.enter()

    def change_state(self, state: State) -> None:
        """
        This should be called in the execute method of the current state: State
        """
        self.next_state = state
