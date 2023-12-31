# another way of importing module
from datetime import datetime,timedelta

from selenium import webdriver


# print current time
print(datetime.now())
print(datetime.now().date()) # to get the date only
print(datetime.now().time())

# date formatting 2023/12/31
curr_dateTime = datetime.now()
print(curr_dateTime.strftime('%Y=%M=%D'))

# suppose we want 10 days after date using timedelta

future_date=curr_dateTime+timedelta(days=10)
print(future_date)
print(future_date.month)
print(future_date.year)

