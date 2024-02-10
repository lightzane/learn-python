# Functions

https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

Functions are basically some instructions packaged together that performs a specific task.

## Blank

A function without any content

```py
def hello_func():
    pass

print(hello_func) # => <function hello_func at 0x00000201A68E8A40>
print(hello_func()) # => None
```

## Non blank

```py
def hello_func():
    print('Hello Function!')

hello_func() # => Hello Function!
```

```py
def hello_func():
    return 'Hello Function!'

print(hello_func()) # => Hello Function!
print(type(hello_func())) # => <class 'str'>
print(hello_func().upper()) # => HELLO FUNCTION!
```

## Passing parameters

```py
def hello(name):
    return f'Hello {name}!'

print(hello('John')) # => Hello John!
```

### default parameter value

```py
def hello(greeting, name = 'You'):
    return f'{greeting} {name}!'

print(hello('hello')) # => hello You!
print(hello('hello', 'John')) # => hello You!
```

## parameters \* and \*\*

`*args` - allow accept an arbritrary number of positional argument
`*kwargs` - allow accept an arbritrary number of keyword argument

```py
def student_info(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

student_info('Math', 'Art', name = 'John', age = 22)
# => args: ('Math', 'Art')
# => kwargs: {'name': 'John', 'age': 22}
```

`args: ('Math', 'Art')` = [tuple](https://github.com/lightzane/learn-python/tree/04/lists-tuples-sets?tab=readme-ov-file#tuples)
`kwargs: {'name': 'John', 'age': 22}` = [dictionary](https://github.com/lightzane/learn-python/tree/05/dictionaries?tab=readme-ov-file#dictionaries)

```py
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
```

# Docstring

Triple quotes = `docstring` is used to document what functions would do

```py
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
```

```py
print(help(is_leap))
# => is_leap(year)
# =>    Return True for leap years, False for non-leap years.
```

The description will match the content that we put inside the `docstring`
