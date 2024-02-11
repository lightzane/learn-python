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

emp_1 = Employee('John', 'Doe', 50)
emp_2 = Employee('Ji-Eun', 'Lee', 100)

print('Num of employees:', Employee.num_of_emps) # => Num of employees: 2

Employee.raise_amount = 1.05
print(Employee.raise_amount) # => 1.05
print(emp_1.raise_amount) # => 1.05
print(emp_1.raise_amount) # => 1.05

emp_1.apply_raise()

print(emp_1.__dict__) # => {'first': 'John', 'last': 'Doe', 'pay': 52, 'email': 'john.doe@company.com'}
print(emp_2.__dict__) # => {'first': 'Ji-Eun', 'last': 'Lee', 'pay': 100, 'email': 'ji-eun.lee@company.com'}

# Notice that there is NO `raise_amount` on the instances' dictionary

emp_1.raise_amount = 2
emp_1.apply_raise()

print(emp_1.__dict__) # => {'first': 'John', 'last': 'Doe', 'pay': 104, 'email': 'john.doe@company.com', 'raise_amount': 2}
