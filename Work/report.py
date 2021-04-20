#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

'''
 define a function read_portfolio(filename) that opens a given portfolio file and 
 reads it and represent each stock in the portfolio with a 
 dictionary.
 In dictionary use the field names of “name”, “shares”, and “price” to represent the 
 different columns in the input file.
 Plus, to work with various input files, but without regard for the actual column number where the name, shares, and price appear...
 using zip() - of the most useful tricks to know about when processing a lot of data files
'''

import sys
import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of Object ('Stock') instances (iterable instances) with
    name, shares, and price. The creation of a Portfolio object (here and in portfolio.py files) was a bit muddled, so now working w/ the Portfolio classmethod created there
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts) # using the Portfolio classmethod 'from_csv'

def read_prices(filename):
    '''Initally read a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices. 
    Now, simply reads a CSV file of price data into a Dict. mapping names to prices.
    '''
    with open(filename) as iterObject:
        return dict(fileparse.parse_csv(iterObject,types=[str,float], has_headers=False))

def make_report(portfolio, price):
    ''' takes a list of stocks and dictionary of prices and returns a list of tuples containing these in rows 
    '''
    report_list = []
    
    for n in portfolio:
        current_price = price[n.name]
        changes = n.price - current_price
        tup = (n.name, n.shares, current_price, changes)
        report_list.append(tup)
        
    return report_list

def print_report(report, formatter):
    ''' calculations asked for report '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
     
    return
    
def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_file)
    price = read_prices(prices_file)
    report = make_report(portfolio, price)
    # print it out:
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

    return
    
def main(args):
    if len(args) not in (3,4):
        raise SystemExit('proper way of using this function:: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])
    
if __name__ == '__main__':
    main(sys.argv)