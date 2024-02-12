# Python Object-Oriented Programming

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'.lower()

        Employee.num_of_emps += 1

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) # this also works
        self.prog_lang = prog_lang

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

dev_1 = Developer('John', 'Doe', 50, 'Typescript and Python')
emp_2 = Employee('Ji-Eun', 'Lee', 50)
mgr_1 = Manager('Robin', 'Nico', 100, [dev_1])
mgr_2 = Employee.from_string('naomi_scott_10', split='_')

# Before __repr__ is defined in the Employee class
print(emp_2) # => <__main__.Employee object at 0x00000194A8D888C0>

# After __repr__ is defined in the Employee class
print(emp_2) # => Employee('Ji-Eun', 'Lee', 50)

# After __str__ is defined in the Employee class
print(emp_2) # => Ji-Eun Lee - ji-eun.lee@company.com

print(repr(emp_2)) # => Employee('Ji-Eun', 'Lee', 50)
print(str(emp_2)) # => Ji-Eun Lee - ji-eun.lee@company.com

print(emp_2.__repr__()) # => Employee('Ji-Eun', 'Lee', 50)
print(emp_2.__str__()) # => Ji-Eun Lee - ji-eun.lee@company.com

print(1+2) # => 3
print(int.__add__(1, 2)) # => 3

print('a' + 'b') # => ab
print(str.__add__('a', 'b')) # => ab

print(len('test')) # => 4
print('test'.__len__()) # => 4

emp_1 = Employee('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 50)

# After __add__ is defined in the Employee class
print(emp_1 + emp_2) # => 100 

# After __len__ is defined in the Employee class
print(len(emp_1)) # => 8