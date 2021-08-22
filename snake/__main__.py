from snake.game import Game, PySnakeGame


def __pysnake_game() -> Game:
    """Returns pysnake game application."""
    return PySnakeGame()


def __easyrun(game: Game) -> None:
    """The program allows to launch snakegame cli application."""
    game.run()


def main() -> None:
    __easyrun(__pysnake_game())


if __name__ == "__main__":
    main()
