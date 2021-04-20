from enum import Enum

"""

"""
class Transaction:
    Code = Enum("BUY", "SELL", "DEPOSIT", "FEE", "DIVIDEND", "UNKNOWN")

    symbol = None
    code = Code.UNKNOWN
    shares = None
    value = None

    def __init__(self, symbol, code, shares, value):
        self.symbol = symbol
        self.code = code
        self.shares = shares
        self.value = value
