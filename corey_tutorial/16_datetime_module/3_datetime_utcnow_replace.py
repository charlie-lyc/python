import datetime
import pytz


date_time = datetime.datetime(2021, 6, 30, 9, 30, 45)
print(date_time)
date_time_utc = datetime.datetime(2021, 6, 30, 9, 30, 45, tzinfo=pytz.UTC)
print(date_time_utc)
print()


now = datetime.datetime.now()
print(now)
now_tz = datetime.datetime.now(tz=pytz.UTC)
print(now_tz)
print()


utcnow = datetime.datetime.utcnow()
print(utcnow)
utcnow_tz = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(utcnow_tz)
print()


corey_time_zone = utcnow_tz.astimezone(pytz.timezone('US/Mountain'))
print(corey_time_zone)

