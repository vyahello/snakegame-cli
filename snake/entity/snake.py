from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable, Any
from snake.control.key import Control, ControlKey
from snake.entity import SNAKE_LENGTH
from snake.environment import MAX_LONGITUDE, MAX_LATITUDE
from snake.entity.body import SnakeBody, Body
from snake.environment.window import Window
from snake.entity.food import Food


class Snake(ABC):
    """Abstract interface for a snake."""

    @abstractmethod
    def score(self) -> str:
        pass

    @abstractmethod
    def eat(self, food: Food) -> None:
        pass

    @abstractmethod
    def collided(self) -> bool:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def direction(self, direction: int) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def head(self) -> Body:
        pass

    @abstractmethod
    def move_up(self) -> None:
        pass

    @abstractmethod
    def move_down(self) -> None:
        pass

    @abstractmethod
    def move_left(self) -> None:
        pass

    @abstractmethod
    def move_right(self) -> None:
        pass


@dataclass
class SnakeSetup:
    """Represents snake game setup item."""

    window: Window
    score: int = 0
    timeout: int = 100
    control: Control = ControlKey()
    direction: int = control.right


class TerminalSnake(Snake):
    """Concrete terminal snake."""

    def __init__(self, longitude: int, latitude: int, window: Window) -> None:
        self._setup = SnakeSetup(window)
        self._body_list: List[Any] = list()
        self._body: Callable[[int], Body] = lambda track: SnakeBody(
            long=longitude - track, lat=latitude
        )
        self._head: Body = SnakeBody(long=longitude, lat=latitude, entity="O")
        self._last_head_location: Tuple[int, int] = (longitude, latitude)
        self._direction_map: Dict[Any, Callable[..., Any]] = {
            self._setup.control.up: self.move_up,
            self._setup.control.down: self.move_down,
            self._setup.control.left: self.move_left,
            self._setup.control.right: self.move_right,
        }
        self.prepare()

    def prepare(self) -> None:
        for track in range(SNAKE_LENGTH, 0, -1):
            self._body_list.append(self._body(track))
        self._body_list.append(self._head)

    def score(self) -> str:
        return f"Your Score : {self._setup.score}"

    def eat(self, food: Food) -> None:
        food.reset()
        body: Body = SnakeBody(*self._last_head_location)
        self._body_list.insert(-1, body)
        self._setup.score += 1
        if self._setup.score % 3 == 0:
            self._setup.timeout -= 5
            self._setup.window.timeout()

    def collided(self) -> bool:
        return any(
            [
                body.location() == self.head().location()
                for body in self._body_list[:-1]
            ]
        )

    def update(self) -> None:
        last_body: SnakeBody = self._body_list.pop(0)
        last_body.longitude = self._body_list[-1].longitude
        last_body.latitude = self._body_list[-1].latitude
        self._body_list.insert(-1, last_body)
        self._last_head_location = self.head().longitude, self.head().latitude
        self._direction_map[self._setup.direction]()

    def direction(self, direction: int) -> None:
        if (
            direction  # pylint:disable=bad-continuation
            != self._setup.control.reverse_direction_map()[  # pylint:disable=bad-continuation
                self._setup.direction
            ]
        ):
            self._setup.direction = direction

    def render(self) -> None:
        for body in self._body_list:
            self._setup.window.add_string(
                body.latitude, body.longitude, body.entity()
            )

    def head(self) -> SnakeBody:
        return self._body_list[-1]

    def move_up(self) -> None:
        self.head().latitude -= 1
        if self.head().latitude < 1:
            self.head().latitude = MAX_LATITUDE

    def move_down(self) -> None:
        self.head().latitude += 1
        if self.head().latitude > MAX_LATITUDE:
            self.head().latitude = 1

    def move_left(self) -> None:
        self.head().longitude -= 1
        if self.head().longitude < 1:
            self.head().longitude = MAX_LONGITUDE

    def move_right(self) -> None:
        self.head().longitude += 1
        if self.head().longitude > MAX_LONGITUDE:
            self.head().longitude = 1
