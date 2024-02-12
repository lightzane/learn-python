# Python Object-Oriented Programming

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        if self.first is None or self.last is None:
            return None

        return f'{self.first}.{self.last}@email.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Doe')

print(emp_1.first) # => John
print(emp_1.email) # => john.doe@email.com
print(emp_1.fullname) # => John Doe

emp_1.first = 'Jim'

print(emp_1.first) # => Jim
print(emp_1.email) # => jim.doe@email.com 
print(emp_1.fullname) # => Jim Doe

emp_1.fullname = 'Ji-Eun Lee'

print(emp_1.first) # => Ji-eun
print(emp_1.email) # => ji-eun.lee@email.com

del emp_1.fullname

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)