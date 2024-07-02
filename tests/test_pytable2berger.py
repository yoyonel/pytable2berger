#!/usr/bin/env python
"""Tests for `pytable2berger` package."""

import secrets
from itertools import chain

from click.testing import CliRunner

from pytable2berger import cli
from pytable2berger.pytable2berger import _random_combination, generate_days_matches  # noqa: PLC2701


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pytable2berger' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_using_combinations_and_berger_table():
    """Test functionnality."""
    secrets.randbelow(1_000_000_000)

    joueurs = ['Captain Brice', 'Julien', 'Lionel', 'Xavier', 'Pol', 'Tristan', 'Fabien', 'Damien', 'Francky', 'Khalil']
    # génération (aléatoire) des combinaisons de tous les matchs possibles sans répétitions
    random_players = _random_combination(joueurs, len(joueurs))
    days_matches = generate_days_matches(random_players)

    n = len(joueurs)

    # on peut générer pour chaque jour la liste des matchs qui font jouer tous les joueurs
    for day_matches in days_matches:
        # tests runtimes

        # le nombre de matchs pour une journée est fixe et égale au nombre de joueurs divisé par deux.
        assert len(day_matches) == n // 2

        # tous les joueurs jouent dans la journée
        assert len(set(sum(day_matches, ()))) == n
        # https://docs.python.org/fr/3/library/itertools.html#itertools.chain
        assert len(set(chain(*day_matches))) == n
