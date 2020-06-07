# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    if number % 2 == 0:
        print('This number is even')
    elif number % 2 != 0:
        print("This number is odd")

is_even(11)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def num_even_or_odd(num):
    if num % 2 == 0:
        print('This number is even')
    elif num % 2 != 0:
        print("This number is odd")