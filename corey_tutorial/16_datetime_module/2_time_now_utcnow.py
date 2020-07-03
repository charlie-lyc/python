import datetime

# hour, minute, second, micro-second
time = datetime.time(9, 30, 45, 990000)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)
print()


date_time = datetime.datetime(2021, 6, 30, 9, 30, 45, 990000)
print(date_time)
print(date_time.date())
print(date_time.time())
print()


time_delta1 = datetime.timedelta(days=7)
print(date_time + time_delta1)
time_delta2 = datetime.timedelta(hours=12)
print(date_time + time_delta2)
print()


today = datetime.datetime.today()
now = datetime.datetime.now()
utcnow = datetime.datetime.utcnow()
print(today)
print(now)
print(utcnow)




