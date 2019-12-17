from snake.environment import WIDTH, HEIGHT, MAX_LONGITUDE, MAX_LATITUDE


def test_env_width() -> None:
    assert WIDTH == 60


def test_env_height() -> None:
    assert HEIGHT == 38


def test_env_mx_long() -> None:
    assert MAX_LONGITUDE == 58


def test_env_mx_lat() -> None:
    assert MAX_LATITUDE == 36
