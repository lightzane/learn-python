import datetime

d = datetime.date(2024, 2, 16)
print(d) # => 2024-02-16

today = datetime.date.today()
print(today) # => 2024-02-16
print(today.year) # => 2024
print(today.month) # => 2
print(today.day) # => 16
print(today.weekday()) # => 4 // Friday
print(today.isoweekday()) # => 5

tdelta = datetime.timedelta(days=7)
# tdelta = datetime.timedelta(7) # This also works

print(today + tdelta) # => 2024-02-23
print(today - tdelta) # => 2024-02-09

from_date = datetime.date(today.year, 2, 14)
IU_bday = datetime.date(today.year, 5, 16)

days_before_bday = IU_bday - from_date
print(days_before_bday) # => 92 days, 0:00:00
print(days_before_bday.days) # => 92
print(days_before_bday.total_seconds()) # => 7948800.0


t = datetime.time(9, 30, 45, 100000)
print(t) # => 09:30:45.100000
print(t.hour) # => 9
print(t.minute) # => 30
print(t.second) # => 45
print(t.microsecond) # => 100000

tdelta = datetime.timedelta(days=7, hours=12)

dt = datetime.datetime(2024, 2, 16, 9, 30, 45, 100000)
print(dt) # => 2024-02-16 09:30:45.100000
print(dt + tdelta) # => 2024-02-23 09:30:45.100000

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.now(datetime.UTC) # Python 3.12+ ?

print(dt_today) # => 2024-02-16 20:17:48.450878
print(dt_now) # => 2024-02-16 20:17:48.450878
print(dt_utcnow) # => 2024-02-16 12:17:48.450878+00:00

import pytz

dt = datetime.datetime(2024, 2, 16, 9, 30, 45, tzinfo=pytz.UTC)
print(dt) # => 2024-02-16 09:30:45+00:00

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow) # => 2024-02-16 12:34:42.500933+00:00

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn) # => 2024-02-16 05:34:42.500933-07:00

dt_kor = dt_utcnow.astimezone(pytz.timezone('Asia/Seoul'))
print(dt_kor) # => 2024-02-16 21:34:42.500933+09:00

for tz in pytz.all_timezones:
    print(tz)

dt_sg = datetime.datetime.now()
dt_kor = dt_sg.astimezone(pytz.timezone('Asia/Seoul')) # Python 3.12

sg_tz = pytz.timezone('Asia/Singapore')
dt_sg_tz_aware = sg_tz.localize(dt_sg)

print(dt_sg) # => 2024-02-16 20:48:06.702406
print(dt_kor) # => 2024-02-16 21:48:06.702406+09:00
print(dt_sg_tz_aware) # => 2024-02-16 20:48:06.702406+08:00

today = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
print(today.isoformat()) # => 2024-02-16T20:48:06.705807+08:00

today = datetime.datetime.now()
print(today.strftime('%B %d, %Y')) # => February 16, 2024

dt_today = datetime.datetime.strptime('February 16, 2024', '%B %d, %Y')
print(dt_today) # => 2024-02-16 00:00:00