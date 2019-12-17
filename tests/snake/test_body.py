import pytest
from snake.entity.body import Body, SnakeBody


_long: int = 10
_lat: int = 5
_entity: str = "x"


@pytest.fixture(scope="module")
def body() -> Body:
    return SnakeBody(_long, _lat, _entity)


def test_long(body: Body) -> None:
    assert body.longitude == 10


def test_lat(body: Body) -> None:
    assert body.latitude == 5


def test_entity(body: Body) -> None:
    assert body.entity() == "x"


def test_location(body: Body) -> None:
    assert body.location() == (10, 5)
