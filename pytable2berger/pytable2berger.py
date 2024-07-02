"""Main module."""

import random
from collections.abc import Iterable
from itertools import combinations


def _random_combination(iterable: Iterable, r: int) -> list:
    """Random selection from itertools.combinations(iterable, r)."""
    pool = tuple(iterable)
    n = len(pool)
    indices = random.sample(range(n), r)
    return [pool[i] for i in indices]


def _compute_day(i: int, j: int, n: int) -> int:
    """Compute day from players indices and round.

    > Soit n joueurs et n-1 rondes,
    > on numérote les joueurs de 1 à n (en général par tirage au sort)
    > et les rondes de 1 à n-1.
    (from : https://fr.wikipedia.org/wiki/Table_de_Berger)
    """
    # => i < j
    i, j = (i, j) if i < j else (j, i)

    # Cas où i≠n et j≠n
    if i != n and j != n:  # noqa: PLR1714
        if i + j - 1 < n:  # noqa: SIM108
            day = i + j - 1
        else:
            day = i + j - n
    # j=n et i<n
    elif 2 * i <= n:
        day = 2 * i - 1
    else:
        day = 2 * i - n
    return day


def generate_days_matches(players: list[str]) -> list[list]:
    """Main EntryPoint."""
    # https://docs.python.org/3/library/itertools.html#itertools.combinations
    combined_matches: list[tuple] = list(combinations(players, 2))

    # mapping between indices (starting to 1) and players name
    map_players = {player_name: id_player for id_player, player_name in enumerate(players, start=1)}

    n = len(players)

    # pre-allocate lists for appending results (days matches)
    days_matches: list[list] = [[] for _ in range(n - 1)]

    for player1_name, player2_name in combined_matches:
        # from players indices and using berger table algorithm we can find the day match (starting to 1)
        day = _compute_day(map_players[player1_name], map_players[player2_name], n)
        # appending result -> day match for a tuple of players
        days_matches[day - 1].append((player1_name, player2_name))

    return days_matches
