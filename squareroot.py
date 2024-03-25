# A program that takes a positive floating-point number as input.
#  Outputs an approximation of its square root. 
# Author: Grace Mary Smyth
# References: geeksforgeeks.org, stack overflow, https://patrickwalls.github.io/mathematicalpython/root-finding/newton/

# Creating a function called sqrt
def sqrt(number):
    root = number / 2.0
    while abs(root * root - number) > 0.0001:
        root = (root + number / root) / 2
    return root

# Taking input from the user
number = float(input("Enter a positive number: "))
result = sqrt(number)
print(f"The square root of {number} is approximately: {result}")