import collections

def last_index(outcome, c):
    """Index of last occurrence of an item in a list or tuple"""
    return len(outcome) - outcome[::-1].index(c)

def valid_series(outcome, *, best_of, hca_wins):
    """Adjust raw outcome to reflect valid playoff series outcome"""
    assert best_of in (5, 7)
    c = 'Y' if hca_wins else 'N'  # Character for counting wins
    wins = 4 if best_of == 7 else 3
    assert outcome.count(c) == wins  # Sanity check the input
    return outcome[:last_index(outcome, c)]

def playoff_outcomes(*, best_of, hca_wins):
    """Possible playoff series outcomes"""
    if best_of not in (5, 7):
        raise ValueError('playoff series must be best of 5 or 7 games')
    if hca_wins:
        yes = 4 if best_of == 7 else 3
        no = best_of - yes
    else:
        no = 4 if best_of == 7 else 3
        yes = best_of - no
    wins = 'Y'*yes + 'N'*no
    raw_outcomes = set(outcome for outcome in itertools.permutations(wins))
    outcomes = {
        valid_series(outcome, best_of=best_of, hca_wins=hca_wins)
        for outcome in raw_outcomes
    }
    return outcomes