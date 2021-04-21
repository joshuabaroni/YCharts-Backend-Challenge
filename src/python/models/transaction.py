from enum import Enum

from src.python.models.position import Position

"""
Data Model for an individual Transaction
"""
class Transaction(Position):

    # todo how to make static in py?
    class Code (Enum):
        BUY = "BUY"
        SELL = "SELL"
        DEPOSIT = "DEPOSIT"
        FEE = "FEE"
        DIVIDEND = "DIVIDEND"
        DEFAULT = "UNKNOWN"

    code = Code.DEFAULT
    value = None

    def __init__(self, symbol, code, shares, value):
        self.symbol = symbol
        self.shares = shares
        self.value = value
        self.code = code if self.Code.__members__ else self.Code.DEFAULT

    def to_string(self):
        return self.symbol + " " + self.code + " " + str(self.shares) + " " + str(self.value)
