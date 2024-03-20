# Programme that outputs whether or not today is a week day
# Author :Grace Mary Smyth
# References:https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python

import datetime

today = datetime.datetime.today()

if today.weekday() ==4:
    print("It is friday, Almost the weekend!!")
elif today.weekday() == 5 or today.weekday() == 6:
    print("Horray! Its the weekend!!")
else:
    days_to_weekend = 4 - today.weekday()
    print(f"{days_to_weekend} days until the weekend.")