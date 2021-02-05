from snake.game import Game, SnakeGame, PySnakeGame


def __pysnake_game() -> Game:
    """Returns pysnake game application."""
    return PySnakeGame()


def __easyrun(game: Game) -> None:
    """The program allows to launch snakegame cli application."""
    game.run()


if __name__ == "__main__":
    __easyrun(game=__pysnake_game())
