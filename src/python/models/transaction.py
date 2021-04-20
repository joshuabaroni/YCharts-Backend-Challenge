from enum import Enum

"""
Data Model for an individual Transaction
"""
class Transaction:

    # todo how to make static in py?
    class Code (Enum):
        BUY = "BUY"
        SELL = "SELL"
        DEPOSIT = "DEPOSIT"
        FEE = "FEE"
        DIVIDEND = "DIVIDEND"
        DEFAULT = "UNKNOWN"

    symbol = None
    code = Code.DEFAULT
    shares = None
    value = None

    def __init__(self, symbol, code, shares, value):
        self.symbol = symbol
        self.shares = shares
        self.value = value
        self.code = code if self.Code.value2member_map_ else self.Code.DEFAULT

    def to_string(self):
        return self.symbol + ":" + self.code + ":" + self.shares + ":" + self.value
