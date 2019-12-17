from snake.entity import SNAKE_LENGTH, SNAKE_LATITUDE, SNAKE_LONGITUDE


def test_snake_length() -> None:
    assert SNAKE_LENGTH == 5


def test_snake_latitude() -> None:
    assert SNAKE_LATITUDE == 3


def test_snake_longitude() -> None:
    assert SNAKE_LONGITUDE == 6
