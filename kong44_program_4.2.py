""""

Eric Kong
1/23/2020
Chapter 4 Exercise 4.2

"""
# import the turtle module 
import turtle

# bob is an object with type Turtle and module turtle
bob = turtle.Turtle()
print(bob)

 # function that takes 3 arguments and draws the petal
def petal(bob, r, angle): 
    for i in range(2):
        bob.circle(r,angle)
        bob.left(180-angle)

# function that takes 4 arguments and draws a flower
# arguments are self, number of petals, radius and angle      
def flower(bob, n, r, angle):
    for i in range(n):
        petal(bob, r, angle)
        bob.left(360/n)

# moving bob to the left so that the image is centered
bob.pu() # pen up
bob.bk(200) # backwards
bob.pd() # pen down

# the first flower in Figure 4.1
flower(bob, 7, 60, 60)

# moving bob to a new location without drawing
bob.pu()
bob.fd(200)
bob.pd()

# the second flower in Figure 4.2
flower(bob, 10, 40, 80)

# moving bob to a new location without drawing
bob.pu()
bob.fd(200)
bob.pd()

# the third flower
flower(bob, 20, 500, 10)

turtle.mainloop()