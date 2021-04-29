# stock.py

from .typedproperty import String, Integer, Float # defined in typedproperty.py to simplify code and eliminate annoying repetition


class Stock:
    #__slots__ = ('name','_shares','price') # (Prior code) allowing certain attr names to be given only
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
        
    @property
    def cost (self):
        return self.shares * self.price
        
    def sell (self, nshares):
        self.shares -= nshares
        return self.shares