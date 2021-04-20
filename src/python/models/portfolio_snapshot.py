
"""
A Snapshot of the portfolio by day. make a new instance per day
"""
class PortfolioSnapshot:

    ownedStocks = {}
    cash = 0

    def __init__(self, **kwargs):
        try:
            self.cash += kwargs.__getitem__("cash")
            self.ownedStocks = kwargs.__getitem__("stocks").values()
        finally:
            print("New Portfolio Object init")

    def reconcile(self, portfolio_snapshot2):
        dif = {}
        if isinstance(portfolio_snapshot2, self.__class__):
            print("checking values...")
            # todo check all values in both portfolio snapshots
            #  add diffs to dif dict
            #  convert dif dict to transaction model?

        return None
