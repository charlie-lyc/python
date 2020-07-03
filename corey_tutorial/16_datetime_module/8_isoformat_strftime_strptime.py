import datetime
import pytz

now_tz = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(now_tz)
print(now_tz.isoformat())
print(now_tz.strftime('%B %d, %Y'))
print()

print(now_tz.strftime('%Y-%m-%d %H:%M:%S'))
print(now_tz.strftime('%B%d,%y %H:%M:%S'))
print()


dt_str = 'June 30, 2020'
# Create date/time object : 주어진 문자열이 날짜시간 데이터의 일정 포맷을 충족시켜야 한다.
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
# Represent date/time object : 날짜시간 데이터를 출력할 때는 변형시킬 수 있다. 
print(dt.strftime('%y-%m-%d'))


# strftime() : Datetime to String
# strptime() : String to Datetime
