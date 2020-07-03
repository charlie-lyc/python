import datetime
import pytz

##################################################################

myTimeNow = datetime.datetime.now() 
print('My   Time    Now :', myTimeNow)
# print(myTimeNow.date())
# print(myTimeNow.time())
# print()

coreyTimeZone = myTimeNow.astimezone(pytz.timezone('US/Mountain'))
print("Corey's Time Now :", coreyTimeZone.date(), coreyTimeZone.time())
# print("Corey's Time Now :", coreyTimeZone)
# print(coreyTimeNow.tzinfo)
# print(coreyTimeNow.tzname())
# print(coreyTimeNow.timetz())

print()

##################################################################

utcTimeNow = datetime.datetime.utcnow()
print('UTC  Time    Now :', utcTimeNow)

utcTimeZone = utcTimeNow.replace(tzinfo=pytz.UTC)
print('UTC  Time   Zone :', utcTimeZone)

### 이렇게 정보를 얻을 수도 있다.
# utcTimeZone = datetime.datetime.now(tz=pytz.UTC)
# print('UTC  Time   Zone :', utcTimeZone)

print()

###################################################################

myTimeZone = utcTimeZone.astimezone(pytz.timezone('Asia/Seoul'))
print('My  Time    Zone :', myTimeZone)

coreyTime_zone = utcTimeZone.astimezone(pytz.timezone('US/Mountain'))
print("Corey's Time Zone:", coreyTime_zone)


###################################################################


# for tz in pytz.all_timezones:
# 	print(tz)


