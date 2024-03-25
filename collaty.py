# Programme that asks the user to input any positive integer
# It then outputs the successive values of the calculation
# The programme end if the current value is one
# Author: Grace Mary Smyth
# References: pythongeeks.org, w3schools.com

number = int(input("Enter an integer: "))

while (number != 1):
# If integer is even, divide by 2
    if number%2==0:
        number = number//2
        print(int(number))

# If integer is odd, multiply by 3
    else: 
         number = number * 3
         print(int(number))


#if integer is one (end)
    if number == 1:
        print("End")
    