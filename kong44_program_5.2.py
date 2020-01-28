""""

Eric Kong
1/22/2020
Chapter 5 Exercise 5.2 

"""
print("Checking to see if Fermat's theorem holds.")

# function that solves part 1 of Exercise 5.2 
# a simple if-else statement that uses conditional logic 
def check_fermat(a,b,c,n):
    if n > 2 and a**n+b**n==c**n: 
        print("Holy smokes, Fermat was wrong!")
        
    else:
        print("\nNo, that doesn't work.")

# function that solves part 2 of exercise 5.2
# prompts the user for inputs and converts them to integers 
def prompt_user():
    a = int(input("Enter a numeric value for parameter 'a'\n >"))
    b = int(input("Enter a numeric value for parameter 'b'\n >"))
    c = int(input("Enter a numeric value for parameter 'c'\n >"))
    n = int(input("Enter a numeric value for parameter 'n'\n >"))
    
    check_fermat(a,b,c,n) # passing arguments to check_fermat
    
# call the prompt user function so it runs 
prompt_user()