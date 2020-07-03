import datetime
import pytz

#############################################################

now = datetime.datetime.now()
my_tz1 = now.astimezone(pytz.timezone('Asia/Seoul'))
print(my_tz1)

now_tz = datetime.datetime.now(tz=pytz.UTC)
my_tz2 = now_tz.astimezone(pytz.timezone('Asia/Seoul'))
print(my_tz2)
print()


# utcnow = datetime.datetime.utcnow()
# my_tz1 = utcnow.astimezone(pytz.timezone('Asia/Seoul'))
# print(my_tz1)

utcnow_tz = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
my_tz2 = utcnow_tz.astimezone(pytz.timezone('Asia/Seoul'))
print(my_tz2)
print()

#############################################################
print('####################################################')
#############################################################

now = datetime.datetime.now()
eastern_tz1 = now.astimezone(pytz.timezone('US/Eastern'))
print(eastern_tz1)

now_tz = datetime.datetime.now(tz=pytz.UTC)
eastern_tz2 = now_tz.astimezone(pytz.timezone('US/Eastern'))
print(eastern_tz2)
print()


# utcnow = datetime.datetime.utcnow()
# eastern_tz1 = utcnow.astimezone(pytz.timezone('US/Eastern'))
# print(eastern_tz1)

utcnow_tz = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
eastern_tz2 = utcnow_tz.astimezone(pytz.timezone('US/Eastern'))
print(eastern_tz2)

##############################################################

# for tz in pytz.all_timezones:
# 	print(tz)





