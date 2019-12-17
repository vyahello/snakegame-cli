from snake.game import Game, SnakeGame


def _run_game(game: Game) -> None:
    """Runs specific game."""
    game.run()


def _run_snake_game() -> None:
    """Runs snake game."""
    _run_game(SnakeGame())


if __name__ == "__main__":
    _run_snake_game()
