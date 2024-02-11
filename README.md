# Class methods and Static methods

https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

Diff methods:

- [Regular Methods](#regular-method) - auto-passes `self` (instance) as first argument
- [Class Methods](#creating-a-class-method) - auto-passes `cls` (class) as first argument
- [Static Methods](#static-method) - does not pass anything, automatically

## Regular method

Automatically passes the instance of class (`self`) as first argument.

```py
class Employee:
    ...
    def fullname(self):
        pass
```

Notice that method's first argument is the `self` or the instance of the class

## Creating a Class Method

Use the `@classmethod` decorator.

Automatically passes the class (`cls`) as first argument.

```py
class Employee:
    ...
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
```

Notice that method's first argument is the `class` itself and NOT self.

**Testing your class**

```py
Employee.set_raise_amount(1)
emp_1.set_raise_amount(1.05)

print(Employee.raise_amount) # => 1.05
print(emp_1.raise_amount) # => 1.05
print(emp_1.raise_amount) # => 1.05
```

## Alternative to constructor

Our current constructor:

```py
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'.lower()

        Employee.num_of_emps += 1
```

There are some use-case that the input is `<first>-<last>-<pay>` string format.

We can create `Class methods` to serve as an alternative on creating an instance of a class.

```py
class Employee:
    ...
    @classmethod
    def from_string(cls, emp_string, split='-'):
        first, last, pay = emp_string.split(split)
        return cls(first, last, int(pay))
```

**Testing your class**

```py
emp_1 = Employee('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 100)
emp_3 = Employee.from_string('robin-nico-70')
emp_4 = Employee.from_string('naomi_scott_10', split='_')
# emp_4 = Employee.from_string('naomi_scott_10', '_') # this also works

print(Employee.num_of_emps) # => 4
print(emp_3.__dict__) # => {'first': 'robin', 'last': 'nico', 'pay': 70, 'email': 'robin.nico@company.com'}
print(emp_4.__dict__) # => {'first': 'naomi', 'last': 'scott', 'pay': 10, 'email': 'naomi.scott@company.com'}
```

## Static Method

Use the `@staticmethod` decorator

Does not automatically pass anything in the argument. Use whenever you do not need to access the `self` (instance of class) or `cls` (class itself) in your arguments.

```py
@staticmethod
    def is_workday():
        pass
```

**Testing your static method**

```py
import datetime

class Employee:
    ...
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2024, 2, 11) # (Sunday)

print(Employee.is_workday(my_date)) # => False
```
