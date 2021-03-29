#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

"""
The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. 
Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).
"""
import report

def portfolio_cost(filename):
    '''
    This function takes a filename as input, reads the portfolio data in that file, and 
    returns the total cost of the portfolio as a float.
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

# pass the name of the file in as an argument
# sys.argv is a list containing passed arguments on the command line (if any). If no arg given through cmd we set here a default file to read (else case)

def main(args):
    if len(args) != 2:
        raise SystemExit('proper way of using this function: %s portfile' % args[0])
    filename = args[1]
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)