# A program that takes a positive floating-point number as input.
#  Outputs an approximation of its square root. 
# Author: Grace Mary Smyth
# References: geeksforgeeks.org, stack overflow, https://patrickwalls.github.io/mathematicalpython/root-finding/newton/


def sqrt(number):
    guess = number / 2.0
    while abs(guess * guess - number) > 0.0001:
        guess = (guess + number / guess) / 2
    return guess

# Taking input from the user
number = float(input("Enter a positive number: "))
result = sqrt(number)
print(f"The square root of {number} is approximately: {result}")