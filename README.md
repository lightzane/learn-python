# Inheritance - Creating Subclasses

https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

Sub-classes of `Employees`:

- [Developer](#developer-class)
- [Manager](#manager-class)

# Developer class

```py
class Developer(Employee):
    pass
```

The `Developer` will inherit all attributes and methods of the `Employee` class.

```py
dev_1 = Developer('John', 'Doe', 50)
print(dev_1.email) # => john.doe@company.com
```

## Help function

```py
class Employee:
    ...

class Developer(Employee):
    pass

dev_1 = Developer('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 50)
emp_3 = Employee.from_string('robin-nico-70')
emp_4 = Employee.from_string('naomi_scott_10', split='_')

print(dev_1.email) # => john.doe@company.com

print(help(Developer)) # => (( see output below ))
```

**OUTPUT**

```bash
john.doe@company.com
Help on class Developer in module __main__:

class Developer(Employee)
 |  Developer(first, last, pay)
 |
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |
 |  Methods inherited from Employee:
 |
 |  __init__(self, first, last, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  apply_raise(self)
 |
 |  fullname(self)
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from Employee:
 |
 |  from_string(emp_string, split='-') from builtins.type
 |
 |  set_raise_amount(amount) from builtins.type
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from Employee:
 |
 |  is_workday(day)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |
 |  num_of_emps = 4
 |
 |  raise_amount = 1.04

None
```

## Increase raise_amount for Developer

```py
class Developer(Employee):
    raise_amount = 1.10

dev_1 = Developer('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 50)

print(dev_1.pay) # => 50
print(emp_2.pay) # => 50

dev_1.apply_raise()
emp_2.apply_raise()

print(dev_1.pay) # => 55
print(emp_2.pay) # => 52
```

## Super

Inheriting the parent's `__init__` constructor while having its own constructor.

```py
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) # this also works
        self.prog_lang = prog_lang
```

# Manager Class

```py
class Manager(Employee):

    '''
    The description for the manager class
    '''

    def __init__(self, first, last, pay, employees=None): # * Practice: Pass "None" instead of empty mutable data types
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
```

**Testing your class**

```py
dev_1 = Developer('John', 'Doe', 50, 'Typescript and Python')
emp_2 = Employee('Ji-Eun', 'Lee', 50)
mgr_1 = Manager('Robin', 'Nico', 100, [dev_1])

mgr_1.add_emp(emp_2)
mgr_1.print_emps()
# => --> John Doe
# => --> Ji-Eun Lee

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
# => --> Ji-Eun Lee
```

# isintance

```py
print(isinstance(mgr_1, Employee)) # => True
print(isinstance(mgr_1, Manager)) # => True
print(isinstance(mgr_1, Developer)) # => False
```

# issubclass

```py
print(issubclass(Manager, Employee)) # => True
print(issubclass(Manager, Developer)) # => False
print(issubclass(Employee, Developer)) # => False
print(issubclass(Developer, Employee)) # => True
```
