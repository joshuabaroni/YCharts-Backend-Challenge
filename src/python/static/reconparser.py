import os

from src.python.models.portfolio_snapshot import PortfolioSnapshot
from src.python.models.transaction_snapshot import TransactionSnapshot
from src.python.static import utils
from src.python.models import stock, transaction


def parse_recon_files(filepaths):
    portfolio = {}  # contains snapshot objects
    portfolio_out = []
    for filepath in filepaths:
        filepath = utils.join_to_relative_path(filepath)
        file = open(filepath, "r")
        if file.name.__contains__("_in"):
            raw = file.readlines(),
            tag = ""
            portfolio_snap = None
            transaction_snap = None
            for content in raw[0]:
                if tag.__contains__("-TRN"):
                    if content.__contains__(" "):
                        if transaction_snap is None:
                            transaction_snap = TransactionSnapshot()
                        transaction_snap.transactions.append(parse_positions_trades(content))
                    else:
                        portfolio[tag] = transaction_snap
                        transaction_snap = TransactionSnapshot()
                        tag = content.split("\n")[0]
                        print(utils.logger_header + "tag: " + tag)
                else:
                    if content.__contains__(" "):
                        if portfolio_snap is None:
                            portfolio_snap = PortfolioSnapshot()
                        portfolio_snap.owned_stocks.append(parse_positions_trades(content))
                    elif portfolio_snap is not None:
                        portfolio[tag] = portfolio_snap
                        portfolio_snap = PortfolioSnapshot()
                        tag = content.split("\n")[0]
                        print(utils.logger_header + "tag: " + tag)
                    else:
                        tag = content.split("\n")[0]
                        print(utils.logger_header + "tag: " + tag)
            portfolio[tag] = portfolio_snap
            portfolio_snap = PortfolioSnapshot()
        elif file.name.__contains__("_out"):
            raw = file.readlines(),
            portfolio_snap = None
            for content in raw[0]:
                if content.__contains__(" "):
                    if portfolio_snap is None:
                        portfolio_snap = PortfolioSnapshot()
                    portfolio_snap.owned_stocks.append(parse_positions_trades(content))
            portfolio_out = portfolio_snap
            print(utils.logger_header + "tag: " + tag)
    print(utils.logger_header + "portfolio_in: " + portfolio.__str__())
    print(utils.logger_header + "portfolio_out: " + portfolio_out.__str__())
    return [portfolio, portfolio_out]


# todo make private
def parse_positions_trades(content):
    temp = content.split(" ")
    if len(temp) == 2:
        s = stock.Stock(temp[0], temp[1].split("\n")[0])
        print(utils.logger_header + "Position: " + s.to_string())
        return s
    elif len(temp) == 4:
        t = transaction.Transaction(temp[0], temp[1], temp[2], temp[3].split("\n")[0])
        print(utils.logger_header + "Transaction: " + t.to_string())
        return t
    return None
