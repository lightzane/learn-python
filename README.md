# `datetime` Module and `pytz`

https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

How to work with Dates, Times, Timedeltas and Timezones

```py
import datetime
```

## Contents

- [Date](#creating-a-date)
  - [Today](#today)
    - [Timedelta](#timedeltas)
      - [Timedelta to Date](#timedelta-to-date)
      - [Date to Timedelta](#date-to-timedelta)
- [Time](#create-a-time)
- [Datetime](#create-a-datetime)
- [Working with Timezones](#pytz---recommended-for-working-with-timezones)
- [Format Time](#format-time)
  - [Format Codes](#format-codes)
  - [Date to String](#to-string)
  - [String to Date](#to-date)

## Creating a date

```py
import datetime

# d = datetime.date(2024, 02, 16) # ! ERROR !
d = datetime.date(2024, 2, 16)
print(d) # => 2024-02-16
```

### Today

```py
import datetime

today = datetime.date.today()
print(today) # => 2024-02-16
print(today.year) # => 2024
print(today.month) # => 2
print(today.day) # => 16
print(today.weekday()) # => 4 // Friday
print(today.isoweekday()) # => 5
```

`weekday()` - `Monday=0` and `Sunday=6`

`isoweekday()` - `Monday=1` and `Sunday=7`

#### Timedeltas

Difference between 2 dates or time.

##### Timedelta to Date

```py
import datetime

today = datetime.date.today()

tdelta = datetime.timedelta(days=7)
# tdelta = datetime.timedelta(7) # This also works

print(today + tdelta) # => 2024-02-23
print(today - tdelta) # => 2024-02-09
```

##### Date to Timedelta

```py
import datetime

from_date = datetime.date(today.year, 2, 14)
IU_bday = datetime.date(today.year, 5, 16)

days_before_bday = IU_bday - from_date
print(days_before_bday) # => 92 days, 0:00:00
print(days_before_bday.days) # => 92
print(days_before_bday.total_seconds()) # => 7948800.0
```

## Create a time

```py
import datetime

t = datetime.time(9, 30, 45, 100000)
print(t) # => 09:30:45.100000
print(t.hour) # => 9
print(t.minute) # => 30
print(t.second) # => 45
print(t.microsecond) # => 100000
```

## Create a datetime

```py
import datetime

tdelta = datetime.timedelta(days=7, hours=12)

dt = datetime.datetime(2024, 2, 16, 9, 30, 45, 100000)
print(dt) # => 2024-02-16 09:30:45.100000
print(dt + tdelta) # => 2024-02-23 09:30:45.100000
```

```py
import datetime

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.now(datetime.UTC) # Python 3.12+ ?

print(dt_today) # => 2024-02-16 20:17:48.450878
print(dt_now) # => 2024-02-16 20:17:48.450878
print(dt_utcnow) # => 2024-02-16 12:17:48.450878+00:00
```

# `pytz` - Recommended for working with Timezones

(**Python 3.5**)

The standard library has timezone class for handling arbitrary fixed offsets from UTC and timezone.utc as UTC timezone instance.

`pytz` library brings the IANA timezone database (also known as the Olson database) to Python and its usage is recommended.

Source: https://docs.python.org/3.5/library/datetime.html

```bash
pip install pytz
```

```py
import pytz

dt = datetime.datetime(2024, 2, 16, 9, 30, 45, tzinfo=pytz.UTC)
print(dt) # => 2024-02-16 09:30:45+00:00

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow) # => 2024-02-16 12:34:42.500933+00:00

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn) # => 2024-02-16 05:34:42.500933-07:00

dt_kor = dt_utcnow.astimezone(pytz.timezone('Asia/Seoul'))
print(dt_kor) # => 2024-02-16 21:34:42.500933+09:00
```

## List all Timezones

```py
import pytz

for tz in pytz.all_timezones:
    print(tz)
```

## `localize`

```py
import datetime
import pytz

dt_sg = datetime.datetime.now()
dt_kor = dt_sg.astimezone(pytz.timezone('Asia/Seoul')) # Python 3.12

sg_tz = pytz.timezone('Asia/Singapore')
dt_sg_tz_aware = sg_tz.localize(dt_sg)

print(dt_sg) # => 2024-02-16 20:48:06.702406
print(dt_kor) # => 2024-02-16 21:48:06.702406+09:00
print(dt_sg_tz_aware) # => 2024-02-16 20:48:06.702406+08:00
```

## Standard Time

```py
import datetime
import pytz

today = datetime.datetime.now(pytz.timezone('Asia/Singapore'))
print(today.isoformat()) # => 2024-02-16T20:48:06.705807+08:00
```

# Format Time

## Format Codes

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

## To String

```py
import datetime

today = datetime.datetime.now()
print(today.strftime('%B %d, %Y')) # => February 16, 2024
```

## To Date

```py
import datetime

dt_today = datetime.datetime.strptime('February 16, 2024', '%B %d, %Y')
print(dt_today) # => 2024-02-16 00:00:00
```
