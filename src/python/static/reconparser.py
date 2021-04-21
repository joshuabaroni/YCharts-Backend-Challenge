import os

from src.python.models.portfolio_snapshot import PortfolioSnapshot
from src.python.models.transaction_snapshot import TransactionSnapshot
from src.python.static import utils
from src.python.models import stock, transaction


# todo account for cash vars
def parse_recon_files(filepaths):
    portfolio = {}  # contains snapshot objects
    for filepath in filepaths:
        filepath = utils.join_to_relative_path(filepath)
        if filepath.__contains__("_in"):  # change to use input file
            file = open(filepath, "r")
            raw = file.readlines(),
            tag = ""
            portfolio_snap = None
            transaction_snap = None
            for content in raw[0]:
                if tag.__contains__("-TRN"):
                    if content.__contains__(" "):
                        if transaction_snap is None:
                            transaction_snap = TransactionSnapshot()
                        transaction_snap = parse_positions_trades(transaction_snap, content)
                    else:
                        portfolio[tag] = transaction_snap
                        transaction_snap = TransactionSnapshot()
                        tag = content.split("\n")[0]
                        print(utils.logger_header + "tag: " + tag)
                else:
                    if content.__contains__(" "):
                        if portfolio_snap is None:
                            portfolio_snap = PortfolioSnapshot()
                        portfolio_snap = parse_positions_trades(portfolio_snap, content)
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
        elif filepath.__contains__("_out"):
            # portfolio = read_outfile(portfolio, filepath)
            write_outfile(portfolio, filepath)
    return portfolio


# writes to outfile
def write_outfile(portfolio, filepath):
    file = open(filepath, 'w+')
    cache = PortfolioSnapshot()
    diff = []  # diffs between records, this is what is printed in outfile. contains snapshots
    for snap in portfolio:
        if isinstance(portfolio[snap], PortfolioSnapshot):
            if len(cache.owned_stocks) == 0:
                cache = portfolio[snap]
            else:
                diff.append(portfolio[snap].reconcile(cache))
                cache = portfolio[snap]
        elif isinstance(portfolio[snap], TransactionSnapshot):
            cache.apply_trades(portfolio[snap])

    for snap in diff:
        file.write(snap.to_string() + "\n")

# reads sample outfile
def read_outfile(portfolio, filepath):
    file = open(filepath, 'r')
    raw = file.readlines()
    portfolio_snap = None
    for content in raw[0]:
        if content.__contains__(" "):
            if portfolio_snap is None:
                portfolio_snap = PortfolioSnapshot()
            portfolio_snap = parse_positions_trades(portfolio_snap, content)
    portfolio["out"] = portfolio_snap
    return portfolio


# todo make private
# check for matching content formats. if no match, return none
def parse_positions_trades(snap, content):
    temp = content.split(" ")
    if len(temp) == 2:  # position format
        s = stock.Stock(temp[0], temp[1].split("\n")[0])
        print(utils.logger_header + "Position: " + s.to_string())
        snap = cash_check_stock(snap, s)
    elif len(temp) == 4:  # transaction format
        t = transaction.Transaction(temp[0], temp[1], temp[2], temp[3].split("\n")[0])
        print(utils.logger_header + "Transaction: " + t.to_string())
        snap = cash_check_transaction(snap, t)
    return snap


def cash_check_stock(snap, s):
    if s.symbol == "Cash":
        snap.cash += float(s.shares)
    else:
        snap.owned_stocks.append(s)
    return snap


def cash_check_transaction(snap, t):
    if t.code == t.Code.FEE.value or t.code == t.Code.BUY.value:
        snap.cash -= float(t.value)
    elif t.code == t.Code.DEPOSIT.value or t.code == t.Code.DIVIDEND.value or t.code == t.Code.SELL.value:
        snap.cash += float(t.value)
    if t.symbol != "Cash":
        snap.transactions.append(t)
    return snap
