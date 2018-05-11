from enum import Enum, auto
from pracpred.ratings import elo

class SimpleNBAElo(elo.Updater):
    """Simple Elo ratings for NBA teams"""
    class GameType(Enum):
        REGULAR = auto()
        PLAYOFF = auto()

    def __init__(self, *, regular_season_hca=69, playoff_hca=93):
        super().__init__(
            calculator=elo.LogisticCalculator(),
            multiplier=elo.ConstantMultiplier(constant=20)
        )
        self.reg_hca = regular_season_hca
        self.post_hca = playoff_hca

    def update(self, *, game_type, home_team, outcome, elo1, elo2):
        """Update Elo ratings"""
        if outcome == elo.MatchOutcome.DRAW:
            raise ValueError('no draws in basketball')
        if game_type == self.GameType.REGULAR:
            hca = self.reg_hca
        elif game_type == self.GameType.PLAYOFF:
            hca = self.post_hca
        else:
            raise ValueError('invalid game type', game_type)
        if home_team == 1:
            adjustment = hca
        elif home_team == 2:
            adjustment = -hca
        else:
            raise ValueError('invalid home team', home_team)
        return super().update(outcome=outcome, elo1=elo1, elo2=elo2, adjustment=adjustment)