"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"
import math
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
def round_up(n, decimal = 0):
        multiplier = 10 ** decimal
        return math.ceil(n * multiplier)/multiplier
y1 = round_up(y,2)
print("x is %d, y is %0.2f, z is \"%s\"" % (x,y,z))

# Use the 'format' string method to print the same thing
print ("x is {}, y is {:.2f}, z is \"{}\"". format(x, y, z))
# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y:0.2f}, z is \"{z}\"")