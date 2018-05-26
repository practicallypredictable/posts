from enum import Enum, auto
from pracpred.ratings import elo

class GameType(Enum):
    REGULAR = auto()
    PLAYOFF = auto()

class SimpleElo(elo.Updater):
    """Simple Elo ratings for NBA teams"""

    def __init__(self, *, regular_season_hca=69, playoff_hca=93):
        super().__init__(
            calculator=elo.LogisticCalculator(),
            multiplier=elo.ConstantMultiplier(constant=20)
        )
        self._reg_hca = regular_season_hca
        self._post_hca = playoff_hca
    
    @property
    def regular_season_hca(self):
        return self._reg_hca
    
    @property
    def playoff_hca(self):
        return self._post_hca

    def update(self, *, game_type, home_team, outcome, elo1, elo2):
        """Update Elo ratings"""
        if outcome == elo.MatchOutcome.DRAW:
            raise ValueError('no draws in basketball')
        if game_type == GameType.REGULAR:
            hca = self.regular_season_hca
        elif game_type == GameType.PLAYOFF:
            hca = self.playoff_hca
        else:
            raise ValueError('invalid game type', game_type)
        if home_team == 1:
            adjustment = hca
        elif home_team == 2:
            adjustment = -hca
        else:
            raise ValueError('invalid home team', home_team)
        return super().update(outcome=outcome, elo1=elo1, elo2=elo2, adjustment=adjustment)