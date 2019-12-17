from abc import ABC, abstractmethod
from typing import Tuple


class Body(ABC):
    """Abstract interface for a body."""

    @property
    @abstractmethod
    def longitude(self) -> int:
        pass

    @property
    @abstractmethod
    def latitude(self) -> int:
        pass

    @abstractmethod
    def location(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def entity(self) -> str:
        pass


class SnakeBody(Body):
    """Represent snake body interfaces."""

    def __init__(self, long: int, lat: int, entity: str = "x") -> None:
        self._longitude: int = long
        self._latitude: int = lat
        self._entity: str = entity

    @property
    def longitude(self) -> int:
        return self._longitude

    @longitude.setter
    def longitude(self, element: int) -> None:
        self._longitude = element

    @property
    def latitude(self) -> int:
        return self._latitude

    @latitude.setter
    def latitude(self, element: int) -> None:
        self._latitude = element

    def entity(self) -> str:
        return self._entity

    def location(self) -> Tuple[int, int]:
        return self._longitude, self._latitude
