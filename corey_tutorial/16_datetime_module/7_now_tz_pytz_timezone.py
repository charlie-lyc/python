import datetime
import pytz

### 내가 있는 지역 현재시간
now = datetime.datetime.now()
print(now)
print()

### UTC 기준 지역 현재시간
# utc_now = datetime.datetime.utcnow()
# print(utc_now)
# print()

### UTC 기준 지역 현재시간 및 타임존
utc_now_tz = datetime.datetime.now(tz=pytz.UTC)
print(utc_now_tz)
print()

### 특정 지역 현재시간 밎 그 타임존 : 결정적으로 이 한줄이면 전세계 모든 곳의 시간을 알 수 있다.
now_tz = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(now_tz)


############################################


# for tz in pytz.all_timezones:
# 	print(tz)


