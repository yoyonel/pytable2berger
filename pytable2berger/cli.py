"""Console script for pytable2berger."""

from importlib.metadata import version

import click

from pytable2berger.pytable2berger import generate_days_matches


@click.command()
@click.version_option(version("pytable2berger"))
@click.argument("players_names", nargs=-1, type=str)
@click.option(
    "--randomize_players_names", is_flag=True, show_default=True, default=False, help="Randomize players names."
)
def main(players_names: list[str], randomize_players_names: bool):
    """Main entrypoint."""
    click.echo("pytable2berger")
    click.echo("=" * len("pytable2berger"))
    click.echo(f"List of players: {players_names}")

    click.echo(generate_days_matches(players_names, randomize_players_names=randomize_players_names))


if __name__ == "__main__":
    main()  # pragma: no cover
