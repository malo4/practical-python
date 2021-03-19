# mortgage.py
#
# Exercise 1.7

""""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.
Calculate the total amount that Dave will have to pay over the life of the mortgage.
Additional question:
How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first five years have already been paid?
"""
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
start_extra_payment = (12 * 5) # 5 years later
end_extra_payment = start_extra_payment + (12 * 4) # from 5th year onwards, and for 4 years time
extra_payment = 1000.0

while principal > 0:
	if (month >= start_extra_payment and month >= end_extra_payment):
		principal = principal - extra_payment
	month = month + 1
	principal = principal * (1+rate/12) - payment
	total_paid = total_paid + payment
	if principal < 0:
		total_paid = total_paid + principal
		principal = 0
	#print out a table showing the month, total paid so far, and the remaining principal
	print (f'Month:{month}, Total paid:${total_paid}, Still left:${principal}')