# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if(x % 2) == 0:
        print("True")
    else:
        print("False")   
is_even(116)  
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even(x):
    if (x % 2) == 0:
        print(f"{x} is Even!")
    else:
        print(f"{x} is odd")
even(num)