""""

Eric Kong
1/23/2020
Chapter 6 Exercise 6.5 

"""
print("Let's calculate the GCD for two values.")

# importing the gcd function from the library
from math import gcd

# function that calculates the greatest common divisor
# takes 2 arguments 
def GCD(a,b):
    print("The value of the GCD is:")
    print(gcd(a,b))

# prompts the user for 2 values
def prompt():
    a = int(input("Enter a numeric value for parameter 'a'\n >"))
    b = int(input("Enter a numeric value for parameter 'b'\n >"))
    
    GCD(a,b) # passing arguments to GCD

# call the prompt function so it runs
prompt()