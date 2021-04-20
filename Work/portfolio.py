# portfolio.py

import fileparse
import stock

class Portfolio:
    # As the Portfolio class is supposed to contain a list of Stock instances:
    def __init__(self):
        self._holdings = []
    # and
    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)
        
    # while, as we want to read a portfolio from a CSV file, make a class method for this:
    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)
                     
        for d in portdicts:
            self.append(stock.Stock(**d)) # Stock(d['name'], d['shares'], d['price']) BEFORE in report.py - dict. expanded into kwargs
        
        return self
        
    # to support iteration:    
    def __iter__(self):
        return self._holdings.__iter__()  
    
    # incl. other special methods (handy to have in a container class):
    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares