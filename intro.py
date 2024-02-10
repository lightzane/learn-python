def hello_func():
    return 'Hello Function!'

print(hello_func()) # => Hello Function!
print(type(hello_func())) # => <class 'str'>
print(hello_func().upper()) # => HELLO FUNCTION!

def hello(greeting, name = 'You'):
    return f'{greeting} {name}!'

print(hello('hello')) # => hello You!
print(hello('hello', 'John')) # => hello You!

def student_info(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

student_info('Math', 'Art', name = 'John', age = 22)
# => args: ('Math', 'Art')
# => kwargs: {'name': 'John', 'age': 22}

courses = ['Math', 'Art']
info = {
    'name': 'John',
    'age': 22
}

student_info(courses, info)
# => args: (['Math', 'Art'], {'name': 'John', 'age': 22})
# => kwargs: {}

student_info(*courses, **info) # to unpack the values
# => args: ('Math', 'Art')
# => kwargs: {'name': 'John', 'age': 22}



# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2024)) # => True
print(is_leap(2025)) # => False
print(days_in_month(2024, 2)) # => 29
print(days_in_month(2025, 2)) # => 28
print(days_in_month(2025, 5)) # => 31

print(help(is_leap))
# => is_leap(year)
# =>    Return True for leap years, False for non-leap years.