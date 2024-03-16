# Weekly tasks 02
# Python bank.py
# Author: Grace Mary Smyth
# Reference PerpBytes Blog, Ankit Kochar(19/11/2022)

x = int(input("Enter amount1(in cent):"))

y = int( input("Enter amount2(in cent):"))
euro = sum([x,y])//100 # // gives the int division
remainder = euro%10    # % gives the remainder


print("Total: €", euro,".",remainder)


