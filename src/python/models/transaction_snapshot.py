"""
A Snapshot of the transactions for a portfolio by day. make a new instance per day
"""
class TransactionSnapshot:

    transactions = []  # list of transactions taken on a given day
    cash = 0

    def __init__(self, **kwargs):
        try:
            self.cash += kwargs.__getitem__("cash")
            self.ownedStocks = kwargs.__getitem__("stocks").values()
        finally:
            print("New Portfolio Object init")