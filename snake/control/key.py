from abc import ABC, abstractmethod
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from typing import Iterable, Dict


class Control(ABC):
    """Abstract interface for a fame control."""

    @property
    @abstractmethod
    def right(self) -> int:
        pass

    @property
    @abstractmethod
    def left(self) -> int:
        pass

    @property
    @abstractmethod
    def down(self) -> int:
        pass

    @property
    @abstractmethod
    def up(self) -> int:
        pass

    @abstractmethod
    def keys(self) -> Iterable[int]:
        pass

    @abstractmethod
    def reverse_direction_map(self) -> Dict[int, int]:
        pass


class ControlKey(Control):
    """Control game key."""

    def __init__(self) -> None:
        self._right: int = KEY_RIGHT
        self._left: int = KEY_LEFT
        self._down: int = KEY_DOWN
        self._up: int = KEY_UP

    @property
    def right(self) -> int:
        return self._right

    @property
    def left(self) -> int:
        return self._left

    @property
    def down(self) -> int:
        return self._down

    @property
    def up(self) -> int:
        return self._up

    def keys(self) -> Iterable[int]:
        return self._right, self._left, self._down, self._up

    def reverse_direction_map(self) -> Dict[int, int]:
        return {
            self._up: self._down,
            self._down: self._up,
            self._left: self._right,
            self._right: self._left,
        }
