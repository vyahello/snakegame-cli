# pylint:disable=bad-continuation
from abc import ABC, abstractmethod
from random import randint
from snake.environment.window import Window


class Food(ABC):
    """Abstract interface for some food."""

    @property
    @abstractmethod
    def longitude(self) -> int:
        pass

    @property
    @abstractmethod
    def latitude(self) -> int:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


class SnakeFood(Food):
    """Snake food interface."""

    def __init__(
        self, window: Window, max_long: int, max_lat: int, entity: str = "x"
    ) -> None:
        self._longitude: int = randint(1, max_long)
        self._latitude: int = randint(1, max_lat)
        self._max_long: int = max_long
        self._max_lat: int = max_lat
        self._entity: str = entity
        self._window = window

    @property
    def longitude(self) -> int:
        return self._longitude

    @property
    def latitude(self) -> int:
        return self._latitude

    def render(self) -> None:
        self._window.add_string(self._latitude, self._longitude, self._entity)

    def reset(self) -> None:
        self._longitude = randint(1, self._max_long)
        self._latitude = randint(1, self._max_lat)
