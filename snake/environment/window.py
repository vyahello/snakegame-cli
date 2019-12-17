from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Any, Callable
from snake.environment.terminal import Environment


class Window(ABC):
    """Abstract interface for a window."""

    @abstractmethod
    def timeout(self) -> None:
        pass

    @abstractmethod
    def keypad(self, key: int = 1) -> None:
        pass

    @abstractmethod
    def border(self, item: int = 0) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def add_string(self, long: int, lat: int, entity: str) -> None:
        pass

    @abstractmethod
    def getch(self) -> int:
        pass


class TerminalWindow(Window):
    """Terminal game window interface."""

    def __init__(self, env: Environment, timeout: int = 100) -> None:
        @lru_cache()
        def _window() -> Any:
            return env.new_window()

        self._timeout: int = timeout
        self._window: Callable[..., Any] = _window

    def timeout(self) -> None:
        self._window().timeout(self._timeout)

    def keypad(self, key: int = 1) -> None:
        self._window().keypad(key)

    def border(self, item: int = 0) -> None:
        self._window().border(item)

    def add_string(self, long: int, lat: int, entity: str) -> None:
        self._window().addstr(long, lat, entity)

    def clear(self) -> None:
        self._window().clear()

    def getch(self) -> int:
        return self._window().getch()
