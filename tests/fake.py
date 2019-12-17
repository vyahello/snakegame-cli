from snake.environment.window import Window


class FakeWindow(Window):
    """Represent fake terminal window."""

    def timeout(self) -> None:
        pass

    def keypad(self, key: int = 1) -> None:
        pass

    def border(self, item: int = 0) -> None:
        pass

    def clear(self) -> None:
        pass

    def add_string(self, long: int, lat: int, entity: str) -> None:
        pass

    def getch(self) -> int:
        pass
