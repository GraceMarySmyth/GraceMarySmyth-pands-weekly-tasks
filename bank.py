# Weekly tasks 02
# Python bank.py
# Author: Grace Mary Smyth
# Reference PerpBytes Blog, Ankit Kochar(19/11/2022)

x = int(input("Enter amount1(in cent):"))

y = int( input("Enter amount2(in cent):"))
sum = sum([x,y])//100 # // gives the int division
remainder = sum%100    # % gives the remainder


print(("Total: €", sum,remainder).format x, .y, sum, remainder))


