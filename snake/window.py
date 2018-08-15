from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Any, Callable
from snake.environment import Environment


class Window(ABC):
    """Abstract interface for a window."""

    @abstractmethod
    def timeout(self) -> Any:
        pass

    @abstractmethod
    def keypad(self, key: int) -> Any:
        pass

    @abstractmethod
    def border(self, item: int) -> Any:
        pass

    @abstractmethod
    def clear(self) -> Any:
        pass

    @abstractmethod
    def add_str(self, first: int, second: int, score: str) -> Any:
        pass

    @abstractmethod
    def getch(self) -> Any:
        pass


class GameWindow(Window):
    """Terminal game window interface."""

    def __init__(self, env: Environment, timeout: int) -> None:

        @lru_cache()
        def _window() -> Any:
            return env.new_window()

        self._timeout: int = timeout
        self._window: Callable[..., Any] = _window

    def timeout(self) -> Any:
        return self._window().timeout(self._timeout)

    def keypad(self, key: int) -> Any:
        return self._window().keypad(key)

    def border(self, item: int) -> Any:
        return self._window().border(item)

    def add_str(self, first: int, second: int, score: int) -> Any:
        return self._window().addstr(first, second, score)

    def clear(self) -> Any:
        return self._window().clear()

    def getch(self) -> Any:
        return self._window().getch()
