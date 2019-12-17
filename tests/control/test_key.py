import pytest
from snake.control.key import Control, ControlKey

_right: int = 261
_left: int = 260
_down: int = 258
_up: int = 259


@pytest.fixture(scope="module")
def control() -> Control:
    return ControlKey()


def test_right(control: Control) -> None:
    assert control.right == _right


def test_left(control: Control) -> None:
    assert control.left == _left


def test_down(control: Control) -> None:
    assert control.down == _down


def test_up(control: Control) -> None:
    assert control.up == _up


def test_keys(control: Control) -> None:
    assert control.keys() == (_right, _left, _down, _up)


def test_len_keys(control: Control) -> None:
    assert len(control.keys()) == 4


def test_reverse_direction_map(control: Control) -> None:
    assert control.reverse_direction_map() == {
        control.up: control.down,
        control.down: control.up,
        control.left: control.right,
        control.right: control.left,
    }


def test_len_reverse_direction_map(control: Control) -> None:
    assert len(control.reverse_direction_map()) == 4
