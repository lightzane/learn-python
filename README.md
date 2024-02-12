# Special (Magic/Dunder) Methods

https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

`__init__` is an example of a special method or dunder

Other common special `dunder` methods are the following:

```py
class Employee:
    ...
    def __repr__(self):
        pass

    def __str__(self):
        pass

emp_2 = Employee('Ji-Eun', 'Lee', 50)
print(emp_2) # => <__main__.Employee object at 0x00000194A8D888C0>

# These are triggered when we run the followin on instances:
repr(emp_2)
str(emp_2)
```

## `__repr__`

- Unambigious representation of the object which is meant to be seen by other `developers`.

- Used by [`__str__`](#__str__) as a fallback when its not defined.

### Before `__repr__` is defined in the Employee class

```py
class Employee:
    ...

emp_2 = Employee('Ji-Eun', 'Lee', 50)
# Before __repr__ is defined in the Employee class
print(emp_2) # => <__main__.Employee object at 0x00000194A8D888C0>
```

### After `__repr__` is defined in the Employee class

```py
class Employee:
    ...
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

emp_2 = Employee('Ji-Eun', 'Lee', 50)
# After __repr__ is defined in the Employee class
print(emp_2) # => Employee('Ji-Eun', 'Lee', 50)
```

## `__str__`

Readable representation of the object which is meant to be displayed for the `end-user`.

### Before `__str__` is defined in the Employee class

```py
class Employee:
    ...
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

emp_2 = Employee('Ji-Eun', 'Lee', 50)
print(emp_2) # => Employee('Ji-Eun', 'Lee', 50)
```

### After `__str__` is defined in the Employee class

```py
class Employee:
    ...
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

emp_2 = Employee('Ji-Eun', 'Lee', 50)
# After __str__ is defined in the Employee class
print(emp_2) # => Ji-Eun Lee - ji-eun.lee@company.com
```

## `repr()` and `str()`

```py
print(repr(emp_2)) # => Employee('Ji-Eun', 'Lee', 50)
print(str(emp_2)) # => Ji-Eun Lee - ji-eun.lee@company.com

print(emp_2.__repr__()) # => Employee('Ji-Eun', 'Lee', 50)
print(emp_2.__str__()) # => Ji-Eun Lee - ji-eun.lee@company.com
```

# Other example of Dunder is `__add__`

```py
print(1+2) # => 3
print(int.__add__(1,2)) # => 3

print('a' + 'b') # => ab
print(str.__add__('a', 'b')) # => ab

print(len('test')) # => 4
print('test'.__len__()) # => 4
```

## Apply the same in the Employee class

```py
class Employee:
    ...
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 50)

# Before __add__ is defined in the Employee class
print(emp_1 + emp_2) # ERROR

# After __add__ is defined in the Employee class
print(emp_1 + emp_2) # => 100

# After __len__ is defined in the Employee class
print(len(emp_1)) # => 8
```

# References

More predefined dunders / special methods:

- https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
