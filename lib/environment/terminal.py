from abc import ABC, abstractmethod
from typing import Any
import curses


class Environment(ABC):
    """Abstract interface for an environment."""

    @abstractmethod
    def init_screen(self) -> None:
        pass

    @abstractmethod
    def beep(self) -> None:
        pass

    @abstractmethod
    def new_window(self) -> Any:
        pass

    @abstractmethod
    def no_echo(self) -> None:
        pass

    @abstractmethod
    def curse_set(self, curse: int = 0) -> None:
        pass

    @abstractmethod
    def end_window(self) -> None:
        pass


class TerminalEnvironment(Environment):
    """Terminal game environment interface."""

    def __init__(self, width: int, height: int) -> None:
        self._width: int = width
        self._height: int = height

    def init_screen(self) -> None:
        curses.initscr()

    def beep(self) -> None:
        curses.beep()

    def new_window(self) -> Any:
        return curses.newwin(self._height, self._width)

    def no_echo(self) -> None:
        curses.noecho()

    def curse_set(self, curse: int = 0) -> None:
        curses.curs_set(curse)

    def end_window(self) -> None:
        curses.endwin()
