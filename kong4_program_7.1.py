""""

Eric Kong
1/23/2020
Chapter 7 Exercise 7.1

"""
# importing math library so that math.sqrt() function can be used
import math

# copied loop from section 7.5 of the book
def mysqrt(a):
    epsilon = 0.001
    x = a/2 # initial estimate 
    while True: # infinite loop
        y = (x + a/x) / 2 # Newton's method
        if abs(y-x) < epsilon:
            return y
            break # break the loop 
        x = y
		      
# a function that prints a table for numbers 1 to 10
def test_square_root():
	print("a	mysqrt(a)           math.sqrt(a)              |Difference|")
	print("-	---------           ------------              ------------")
	for a in range(1, 10):
		print("%.1f	%.9f	     %.9f	     %.9f" % (a,mysqrt(a), math.sqrt(a), abs(mysqrt(a)-math.sqrt(a))))

# call the function so it runs		
test_square_root()