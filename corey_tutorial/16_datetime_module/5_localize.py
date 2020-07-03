import datetime
import pytz


now = datetime.datetime.now()

now_tz = pytz.timezone('Asia/Seoul')        
mountain_tz = pytz.timezone('US/Mountain') 

############################################

print(now_tz.localize(now))
# print(now_tz.localize(now).date())
# print(now_tz.localize(now).time())
# print(now_tz.localize(now).tzinfo)


print(now.astimezone(now_tz))
# print(now.astimezone(now_tz).date())
# print(now.astimezone(now_tz).time())
# print(now.astimezone(now_tz).tzinfo)
print()

############################################

### pytz.timezone().localize() : XXX
# print(mountain_tz.localize(now))

### datetime.datetime.now().astimezone(pytz.timezone('타임존'))
print(now.astimezone(mountain_tz))

print()

############################################


# for tz in pytz.all_timezones:
# 	print(tz)
