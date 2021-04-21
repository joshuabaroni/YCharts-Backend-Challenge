from src.python.models.daily_snapshot import DailySnapshot
from src.python.models.stock import Stock
from src.python.static import utils
from Lib import operator

"""
A Snapshot of the portfolio by day. make a new instance per day
"""
class PortfolioSnapshot(DailySnapshot):

    # todo can be optimized with stock, shares as dict
    owned_stocks = []

    def __init__(self):
        self.owned_stocks = [] # deconstruct existing object by clearing owned_stocks cache
        print(utils.logger_header + "PortfolioSnapshot cache cleared")

    # returns portfolio_snapshot of diffs
    def reconcile(self, portfolio_snapshot):
        diff_portfolio = PortfolioSnapshot()

        # make dict representation of owned_stock list
        stocks_kv = {}
        for stock in self.owned_stocks:
            stocks_kv[stock.symbol] = float(stock.shares)

        # execute transactions
        for stock in portfolio_snapshot.owned_stocks:
            if not stocks_kv.__contains__(stock.symbol):
                stocks_kv[stock.symbol] = float(0)
            stocks_kv[stock.symbol] = stocks_kv[stock.symbol] - float(stock.shares)
            if stocks_kv[stock.symbol] == 0:
                stocks_kv.pop(stock.symbol)

        # convert back to owned_stock list
        for key in stocks_kv:
            s = Stock(key, stocks_kv[key])
            diff_portfolio.owned_stocks.append(s)

        diff_portfolio.cash = abs(self.cash - portfolio_snapshot.cash)
        return diff_portfolio

    def apply_trades(self, transaction_snapshot):
        # todo optimize with dict instead of stock model. complexity is too high right now 3n and can be reduced to n
        # make dict representation of owned_stock list
        stocks_kv = {}
        for stock in self.owned_stocks:
            stocks_kv[stock.symbol] = float(stock.shares)

        # execute transactions
        for transaction in transaction_snapshot.transactions:
            if not stocks_kv.__contains__(transaction.symbol):
                stocks_kv[transaction.symbol] = float(0)  # init new trade
            if transaction.code == transaction.Code.BUY.value:
                stocks_kv[transaction.symbol] += float(transaction.shares)
            elif transaction.code == transaction.Code.SELL.value:
                stocks_kv[transaction.symbol] -= float(transaction.shares)
            if stocks_kv[transaction.symbol] == 0:
                stocks_kv.pop(transaction.symbol)

        # convert back to owned_stock list
        stock_list = []
        for key in stocks_kv:
            s = Stock(key, stocks_kv[key])
            stock_list.append(s)

        self.cash += transaction_snapshot.cash
        self.owned_stocks = stock_list

    def to_string(self):
        out_str = "Cash " + str(self.cash) + "\n"
        for s in self.owned_stocks:
            out_str += s.to_string() + "\n"
        return out_str
