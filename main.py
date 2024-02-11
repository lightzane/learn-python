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

print(dev_1.email) # => john.doe@company.com

# print(help(Developer))

print(dev_1.pay) # => 50
print(emp_2.pay) # => 50

dev_1.apply_raise()
emp_2.apply_raise()

print(dev_1.pay) # => 55
print(emp_2.pay) # => 52

print(dev_1.__dict__)
print(mgr_1.__dict__)

mgr_1.add_emp(emp_2)
mgr_1.print_emps()
# => --> John Doe
# => --> Ji-Eun Lee

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
# => --> Ji-Eun Lee

# * isinstance
print(isinstance(mgr_1, Employee)) # => True
print(isinstance(mgr_1, Manager)) # => True
print(isinstance(mgr_1, Developer)) # => False

# * issubclass
print(issubclass(Manager, Employee)) # => True
print(issubclass(Manager, Developer)) # => False
print(issubclass(Employee, Developer)) # => False
print(issubclass(Developer, Employee)) # => True

# print(help(Manager))