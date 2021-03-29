#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

'''
 define a function read_portfolio(filename) that opens a given portfolio file and 
 reads it and represent each stock in the portfolio with a 
 dictionary (instead of a tuple used initially). 
 In dictionary use the field names of “name”, “shares”, and “price” to represent the 
 different columns in the input file.
 Plus, to work with various input files, but without regard for the actual column number where the name, shares, and price appear...
 using zip() - of the most useful tricks to know about when processing a lot of data files
'''

import sys
import fileparse

def read_portfolio(filename):
    ''' Initially computed manually the total cost (shares*price) of a portfolio file
    Now, simply reads a stock portfolio file into a List of dictionaries with keys: name, shares, and price.
    '''
    with open(filename) as iterObject:
        return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    

def read_prices(filename):
    '''Initally read a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices. 
    Now, simply reads a CSV file of price data into a Dict. mapping names to prices.
    '''
    with open(filename) as iterObject:
        return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report(portfolio, price):
    ''' takes a list of stocks and dictionary of prices and returns a list of tuples containing these in rows 
    '''
    report_list = []
    
    for n in portfolio:
        current_price = price[n['name']]
        changes = n['price'] - current_price
        tup = (n['name'], n['shares'], current_price, changes)
        report_list.append(tup)
        
    return report_list

def print_report(report):
    ''' calculations asked for report '''
    #Suppose you had a tuple of header names like this:
    headers_tup = ('Name', 'Shares', 'Price', 'Change')
    
    # take the above tuple of headers and create a string where each header name is right-aligned in a 10-character wide field:
    print('%10s %10s %10s %10s' % headers_tup)
    
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)
        
    return
    
def portfolio_report(portfolio_file, prices_file):
    ''' A top-level function for Report program execution - simply execute all of the steps involved in this program '''
    portfolio = read_portfolio(portfolio_file)
    price = read_prices(prices_file)
    report = make_report(portfolio, price)
    print_report(report)
    
    return
    
def main(args):
    if len(args) != 3:
        raise SystemExit('proper way of using this function:: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])
    
if __name__ == '__main__':
    main(sys.argv)