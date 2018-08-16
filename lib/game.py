from abc import ABC, abstractmethod
from curses import (
    KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
)
from lib.environment import WIDTH, HEIGHT, MAX_LONGITUDE, MAX_LATITUDE
from lib.environment.terminal import TerminalEnvironment, Environment
from lib.snake.food import SnakeFood, Food
from lib.environment.window import Window, TerminalWindow
from lib.snake import SNAKE_LONGITUDE, SNAKE_LATITUDE
from lib.snake.snake import Snake, TerminalSnake


class Game(ABC):
    """Abstract interface for a game."""

    @abstractmethod
    def run(self) -> None:
        pass


class SnakeGame(Game):
    """Represent terminal snake game."""

    def __init__(self) -> None:
        self._terminal: Environment = TerminalEnvironment(width=WIDTH, height=HEIGHT)
        self._window: Window = TerminalWindow(env=self._terminal)
        self._snake: Snake = TerminalSnake(longitude=SNAKE_LONGITUDE, latitude=SNAKE_LATITUDE, window=self._window)
        self._food: Food = SnakeFood(window=self._window, max_long=MAX_LONGITUDE, max_lat=MAX_LATITUDE)

    def run(self) -> None:
        self._terminal.init_screen()
        self._terminal.beep()
        self._terminal.beep()
        self._terminal.no_echo()
        self._terminal.curse_set()

        self._window.timeout()
        self._window.keypad()
        self._window.border()

        while True:
            self._window.clear()
            self._window.border(item=0)
            self._snake.render()
            self._food.render()
            self._window.add_str(long=0, lat=5, entity=self._snake.score())
            event: int = self._window.getch()

            if event == 27:
                break

            if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                self._snake.direction(event)

            if (
                    self._snake.head().longitude == self._food.longitude
                    and self._snake.head().latitude == self._food.latitude
            ):
                self._snake.eat(self._food)

            if event == 32:
                key: int = -1
                while key != 32:
                    key = self._window.getch()

            self._snake.update()
            if self._snake.collided():
                break

        self._terminal.end_window()
