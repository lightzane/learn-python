# Property Decorators - Getters, Setters, and Deleters

https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

## Property Decorators

- [Getters](#getters) - `@property`
- [Setters](#setters) - `@<prop_name>.setter`
- [Deleters](#deleters) - `@<prop_name>.deleter`

## Scenario without Getters and Setters

```py
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@email.com'.lower()

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('John', 'Doe')

print(emp_1.first) # => John
print(emp_1.email) # => john.doe@email.com
print(emp_1.fullname()) # => John Doe

emp_1.first = 'Jim'

print(emp_1.first) # => Jim
print(emp_1.email) # => john.doe@email.com # ! Observe that this is still John
print(emp_1.fullname()) # => Jim Doe
```

### Problem #1

Observe that after changing `emp_1.first` to `Jim`...<br>
The `emp_1.email` still have the `John`

### Workaround

```diff
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
-       self.email = f'{self.first}.{self.last}@email.com'.lower()

+   def email(self):
+       return f'{self.first}.{self.last}@email.com'.lower()

    def fullname(self):
        return f'{self.first} {self.last}'

 emp_1 = Employee('John', 'Doe')

 print(emp_1.first) # => John
+print(emp_1.email()) # => john.doe@email.com
-print(emp_1.email) # => john.doe@email.com
 print(emp_1.fullname()) # => John Doe

 emp_1.first = 'Jim'

 print(emp_1.first) # => Jim
+print(emp_1.email()) # => jim.doe@email.com
-print(emp_1.email) # => jim.doe@email.com
 print(emp_1.fullname()) # => Jim Doe
```

In this approach, when we update the `emp_1.first`, then it will also automatically update `emp_1.email()`

### Problem #2 and Solution

Notice, also, `emp_1.email` is changed to `emp_1.email()`

After this approach, anyone that uses our existing code will have to update their code.<br>
So in order to continuously accessing the `email` as an attribute rather than a method `email()`...

We will use `@property` decorator

#### Getters

```diff
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

+   @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'.lower()

    def fullname(self):
        return f'{self.first} {self.last}'

 emp_1 = Employee('John', 'Doe')

 print(emp_1.first) # => John
+print(emp_1.email) # => john.doe@email.com
-print(emp_1.email()) # => john.doe@email.com
 print(emp_1.fullname()) # => John Doe

 emp_1.first = 'Jim'

 print(emp_1.first) # => Jim
+print(emp_1.email) # => jim.doe@email.com
-print(emp_1.email()) # => jim.doe@email.com
 print(emp_1.fullname()) # => Jim Doe
```

**It works also on the fullname()**

```diff
class Employee:
    ...
-   @property
    def fullname(self):
        return f'{self.first} {self.last}'

 emp_1 = Employee('John', 'Doe')
-print(emp_1.fullname())
+print(emp_1.fullname)
```

## Next Scenario

When we update `emp_1.fullname` with a new value<br>
Then we also want to update the `first` and `last` name.

To solve this, we need to create a `@<prop>.setter` decorator

#### Setters

```diff
class Employee:
    ...

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

+   @fullname.setter
+   def fullname(self, new_name):
+       first, last = new_name.split(' ')
+       self.first = first
+       self.last = last

 print(emp_1.first) # => Jim
 print(emp_1.email) # => jim.doe@email.com
 print(emp_1.fullname) # => Jim Doe

+emp_1.fullname = 'Ji-Eun Lee'

+print(emp_1.first) # => Ji-eun
+print(emp_1.email) # => ji-eun.lee@email.com
```

#### Deleters

```py
class Employee:
    ...

    @property
    def email(self):
        if self.first is None or self.last is None:
            return None

        return f'{self.first}.{self.last}@email.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.first = None
        self.last = None

print(emp_1.first) # => Ji-eun
print(emp_1.email) # => ji-eun.lee@email.com

del emp_1.fullname

print(emp_1.first) # => None
print(emp_1.last) # => None
print(emp_1.email) # => None
```
