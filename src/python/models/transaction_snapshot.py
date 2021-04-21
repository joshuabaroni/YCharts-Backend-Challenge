from src.python.static import utils

"""
A Snapshot of the transactions for a portfolio by day. make a new instance per day
"""
from src.python.models.daily_snapshot import DailySnapshot


class TransactionSnapshot(DailySnapshot):

    transactions = []  # list of transactions taken on a given day

    def __init__(self):
        transactions = [] # deconstruct existing object by clearing transaction cache
        print(utils.logger_header + "TransactionSnapshot cache cleared")

    def to_string(self):
        out_str = "Cash " + str(self.cash) + "\n"
        for t in self.transactions:
            out_str += t.to_string() + "\n"
        return out_str


