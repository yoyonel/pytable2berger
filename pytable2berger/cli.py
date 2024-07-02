"""Console script for pytable2berger."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("pytable2berger")
    click.echo("=" * len("pytable2berger"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
