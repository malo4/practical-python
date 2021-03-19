# bounce.py
#
# Exercise 1.5

height = 100 # var to keep the height. starts from 100m
i = 0 
for i in range(0,10):
	height = height * 3/5
	# clean up the output a bit if you use the round() function (say to 4 digits):
	h = round(height,4)
	print(h)
