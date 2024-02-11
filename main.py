# Python Object-Oriented Programming

import datetime

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'.lower()

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string, split='-'):
        first, last, pay = emp_string.split(split)
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 100)
emp_3 = Employee.from_string('robin-nico-70')
emp_4 = Employee.from_string('naomi_scott_10', split='_')

print(Employee.num_of_emps) # => 4

Employee.set_raise_amount(1)
emp_1.set_raise_amount(1.05)

print(Employee.raise_amount) # => 1.05
print(emp_1.raise_amount) # => 1.05
print(emp_1.raise_amount) # => 1.05

print(emp_3.__dict__) # => {'first': 'robin', 'last': 'nico', 'pay': 70, 'email': 'robin.nico@company.com'}
print(emp_4.__dict__) # => {'first': 'naomi', 'last': 'scott', 'pay': 10, 'email': 'naomi.scott@company.com'}

my_date = datetime.date(2024, 2, 11) # (Sunday)

print(Employee.is_workday(my_date)) # => False