# Weekly Task 3
# A python programme tha reads in a 10 character account number
# but only outputs the account number with only the last 4 digits showing.

# Author: Grace Mary Smyth

account = input("account number: ")


print("For security reasons your account number will be displayed as: ")
print("XXXXXX",(account[-4:]))