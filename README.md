# Dictionaries

Working with `key-value` pairs

https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

```py
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
# get(self, key, default=None, /)
# Return the value for key if key is in the dictionary, else default.
```

## Updating dictionary

```py
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
```

```py
student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

age = student.pop('age')
print(age) # => 25
print(student) # => {'name': 'John', 'courses': ['Math', 'CompSci'], 'phone': '888-8888'}
```

## Get keys, values and items

```py
student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

print(len(student)) # => 3
print(student.keys()) # => dict_keys(['name', 'age', 'courses'])
print(student.values()) # => dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items()) # => dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])
```

## Loop

```py
for key, value in student.items():
    print(key, value)
# => name John
# => age 25
# => courses ['Math', 'CompSci']
```
