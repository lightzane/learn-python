# Classes and Instances

https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

## Object-Oriented Programming

**Class** - blueprint for creating instances

## Creating an Empty Class

```py
class Employee:
    pass
```

## Creating a Class

```py
class Employee:
    # constructor()
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'.lower()

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# emp_1 and emp_2 are instances of Employee
emp_1 = Employee('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 100)

print(emp_1.email) # => john.doe@company.com
print(emp_2.email) # => ji-eun.lee@company.com

print(emp_1.fullname()) # => John Doe
print(emp_2.fullname()) # => Ji-Eun Lee

print(Employee.fullname(emp_1)) # => John Doe
print(Employee.fullname(emp_2)) # => Ji-Eun Lee
```
