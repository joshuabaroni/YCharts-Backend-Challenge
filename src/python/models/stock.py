
"""
 <string, number> share ticker, value
"""
class Stock:
    symbol = ""
    value_per_share = 0

    def __init__(self, symbol, value_per_share):
        self.symbol = symbol
        self.value_per_share = value_per_share

    def __init__(self, symbol, shares, value):
        self.symbol = symbol
        self.__init__(self, symbol, value / shares)
