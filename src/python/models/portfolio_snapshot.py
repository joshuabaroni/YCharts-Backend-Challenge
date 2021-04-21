from src.python.models.daily_snapshot import DailySnapshot
from src.python.static import utils

"""
A Snapshot of the portfolio by day. make a new instance per day
"""
class PortfolioSnapshot(DailySnapshot):

    owned_stocks = []

    def __init__(self):
        self.owned_stocks = [] # deconstruct existing object by clearing owned_stocks cache
        print(utils.logger_header + "PortfolioSnapshot cache cleared")

    def reconcile(self, portfolio_snapshot2):
        dif = {}
        if isinstance(portfolio_snapshot2, self.__class__):
            print("checking values...")
            # todo check all values in both portfolio snapshots
            #  add diffs to dif dict
            #  convert dif dict to transaction model?

        return None
