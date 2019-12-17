import pytest
from snake.control.key import Control
from snake.entity.snake import SnakeSetup
from snake.environment.window import Window
from tests.fake import FakeWindow


@pytest.fixture(scope="module")
def setup() -> SnakeSetup:
    return SnakeSetup(FakeWindow())


def test_window(setup: SnakeSetup) -> None:
    assert isinstance(setup.window, Window)


def test_score(setup: SnakeSetup) -> None:
    assert setup.score == 0


def test_timeout(setup: SnakeSetup) -> None:
    assert setup.timeout == 100


def test_control(setup: SnakeSetup) -> None:
    assert isinstance(setup.control, Control)


def test_direction(setup: SnakeSetup) -> None:
    assert setup.direction == 261
