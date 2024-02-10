student = {
    'name': 'John', 
    'age': 25, 
    'courses': ['Math', 'CompSci']
}

print(student) # => {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name']) # => John
print(student['courses']) # => ['Math', 'CompSci']
# print(student['phone']) # ! ERROR ! KeyError: 'phone'
print(student.get('phone')) # => None
print(student.get('phone', 'Not Found')) # => Not Found

student['name'] = 'IU'
student['phone'] = '555-5555'
print(student) # => {'name': 'IU', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

student.update({
    'name': 'John',
    'phone': '888-8888'
})
print(student) # => {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '888-8888'}

del student['age']
print(student) # => {'name': 'John', 'courses': ['Math', 'CompSci'], 'phone': '888-8888'}

student['age'] = 25

age = student.pop('age')
print(age) # => 25
print(student) # => {'name': 'John', 'courses': ['Math', 'CompSci'], 'phone': '888-8888'}

# Reset

student = {
    'name': 'John', 
    'age': 25, 
    'courses': ['Math', 'CompSci']
}

print(len(student)) # => 3
print(student.keys()) # => dict_keys(['name', 'age', 'courses'])
print(student.values()) # => dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items()) # => dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

for key, value in student.items():
    print(key, value)
# => name John
# => age 25
# => courses ['Math', 'CompSci']
