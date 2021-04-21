# YCharts-Backend-Challenge
### Soluton By: Joshua Baroni
The 2nd round interview project for the Data Engineer role at YCharts

## Installation and Run Guide:
Installing python
[Windows](https://docs.python.org/3/using/windows.html)
[Mac](https://docs.python.org/3/using/mac.html)

### Clone private repo
```console
$ git clone https://github.com/joshuabaroni/YCharts-Backend-Challenge.git
```

### CD to base directory
```console
$ cd <path/to/clone/destination>/YCharts-Backend-Challenge
```

### Run this project
```console
$ python -m src.python.main src/resources/input/recon_in.txt src/resources/output/rec
on_out.txt
```

Following the above python command, you will see an output of your data at:

*YCharts-Backend-Challenge/src/resources/recon_out.txt*

## Theory
My approach to this project is as follows:
1) Every day's portfolios and transactions are denoted  by new snapshot instances
    - The PortfolioSnapshot model implements the apply_trades() and reconcile() methods
      - ps.apply_trades() takes a transaction snapshot and returns a copy of the host ps instance with transactions applied to it
      - ps.reconcile() takes a second ps, compares its positions to the host ps instance, and returns any discrepancies
    - Each instance conatins a list of stocks held and transactions made by the portfolio on a given day
2) Parse data into models (Position, Transaction and Stock)
    - Position abstract model contains *stock.symbol* and *stock.shares* which reconcile positions to one another
    - Transaction model contains two additional attributes
      - Enum *transaction.code* of type *Transaction.Code* denoting one of the 5 types of transactions to be made
        - Defaults to "Code.DEFAULT" if an unknown transaction is attempted
      - Value which denotes the monetary value of the position
3) Cache/dict called portfolio that stores all snapshots of positions that have been held over the history of the portfolio
4) Recon Parser
   - Reads positions from the recon.in
   - Writes out the differences observed by ps.reconcile() to recon.out
   
### Potential Improvements
- Refactor functions out of reconparser into private visibility within the models
- Remove Stock models entirely and use dictionaries instead to map symbols to shares for improved algo speed
  - currently deep copies from list\[Stock] to dict{str, float} and back add an extra 2n to the complexity of ps.apply_trades() and ps.reconcile().
  - Altering the fundamental data type of ps.owned_stocks from list to dict would remove this extra complexity
- Removing the need to instantiate models at allgi and using raw data types would flatten the algorithm a bit