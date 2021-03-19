# pcost.py
#
# Exercise 1.27

"""
The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. 
Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).
"""
import sys
import csv

def portfolio_cost(filename):
	'''
	This function takes a filename as input, reads the portfolio data in that file, and 
	returns the total cost of the portfolio as a float.
	'''
	total_cost = 0
	with open(filename, 'rt') as file:
		rows = csv.reader(file)
		headers = next(file) #skip headers
		for line in rows: 
			# error handling via try - except statement:
			try:
			    nshares = int(line[1]) 
			except ValueError:
			    print("Couldn't parse", line)
			price = float(line[2]) # As is the case w/ nshares... there are taken as str. So, convert into INT, Float etc.
			cost = nshares * price
			total_cost = total_cost + cost
	return total_cost

# pass the name of the file in as an argument
# sys.argv is a list containing passed arguments on the command line (if any). If no arg given through cmd we set here a default file to read (else case)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv' 

cost = portfolio_cost(filename)
print('Total cost:', cost)