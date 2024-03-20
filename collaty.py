# Programme that asks the user to input any positive integer
# It then outputs the successive values of the calculation
# The programme end if the current value is one
# Author: Grace Mary Smyth
# References: pythongeeks.org, w3schools.com

number = int(input("Enter an integer: "))
evennum = number/2
oddnum = number*3 

# If integer is even, divide by 2
if (number%2==0):
    print(int(evennum))

# If integer is odd, multiply by 3
else: 
    print(int(oddnum))

# A while loop
while (number != 1):
    continue
    print[number]


#if integer is one (end)
if number == 1: 
    break
else:
    print("End")
    