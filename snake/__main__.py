import click
from snake.game import Game, SnakeGame


@click.command()
@click.option("--run", "-r", default=False, show_default=True, is_flag=True, help="Run an application")
@click.option("--name", "-n", default="pysnake", show_default=True, help="Name of an application")
def easyrun(run: bool, name: str) -> None:
    """The program allows to launch snakegame cli application."""
    game: Game = SnakeGame(name)
    if run:
        print(f"Running {game.name()}")
        game.run()
    else:
        print(f"{' Nothing to run ':=^50}")
        context: click.Context = click.get_current_context()
        click.echo(context.get_help())
        context.exit(0)


if __name__ == "__main__":
    easyrun()  # pylint: disable=no-value-for-parameter
