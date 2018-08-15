from abc import ABC, abstractmethod
from typing import Any
import curses


class Environment(ABC):
    """Abstract interface for an environment."""

    @abstractmethod
    def init_screen(self) -> Any:
        pass

    @abstractmethod
    def beep(self) -> Any:
        pass

    @abstractmethod
    def new_window(self) -> Any:
        pass

    @abstractmethod
    def no_echo(self) -> Any:
        pass

    @abstractmethod
    def curse_set(self, curse: int) -> Any:
        pass

    @abstractmethod
    def end_window(self) -> Any:
        pass


class GameEnvironment(Environment):
    """Terminal game screen interface."""

    def __init__(self, hight: int, width: int) -> None:
        self._hight: int = hight
        self._width: int = width

    def init_screen(self) -> Any:
        return curses.initscr()

    def beep(self) -> Any:
        return curses.beep()

    def new_window(self) -> Any:
        return curses.newwin(self._hight, self._width)

    def no_echo(self) -> Any:
        return curses.noecho()

    def curse_set(self, curse: int) -> Any:
        return curses.curs_set(curse)

    def end_window(self) -> Any:
        return curses.endwin()
