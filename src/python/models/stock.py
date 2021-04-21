
"""
 <string, number> share ticker, value
"""
class Stock:
    symbol = ""
    shares = None
    # value_per_share = None # UNKNOWN

    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

    # def __init__(self, symbol, shares, value):
    #     self.__init__(self, symbol, shares)
    #     self.value_per_share = value / shares

    def to_string(self):
        return self.symbol + " " + str(self.shares)
