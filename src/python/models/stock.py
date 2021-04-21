
"""
 <string, number> share ticker, value
"""
from src.python.models.position import Position


class Stock(Position):

    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

    def to_string(self):
        return self.symbol + " " + str(self.shares)
