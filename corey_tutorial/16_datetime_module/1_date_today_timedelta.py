import datetime

# year, month, day
date = datetime.date(2021, 6, 30)
print(date)
print(date.year)
print(date.month)
print(date.day)
print()


### SyntaxError
# datet


today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday()) # 0 ~ 6 : Monday ~ Sunday
print(today.isoweekday()) # 1 ~ 7 : Monday ~ Sunday
print()


# date2 = date1 + timedelta
# timedelta = date2 - date1
# or
# date2 = date1 - timedelta
# timedelta = date1 - date2


time_delta = datetime.timedelta(days=7)
print(today + time_delta)
print(today - time_delta)
print()


birthday = datetime.date(2021, 6, 30)
till_birthday = birthday - today
print(till_birthday)
print(till_birthday.days)
print(till_birthday.total_seconds())

