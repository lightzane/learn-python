# Conditionals and Booleans

https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

```py
language = 'Python'

if True:
    print('Conditional was True')

if language == 'Python':
    print('Conditional was True')
```

## Comparisons

```py
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Lesser or Equal:  <=
# Object Identity:  is

if language == 'Python':
    print('Language is Python')
else:
    print('No match')
# => Language is Python
```

## elif and else

`elif` = else if

```py
if language == 'Python':
    print('Language is Python')
elif language == 'Typescript':
    print('Language is Javascript with Typescript')
else:
    print('No match')
```

## and

```py
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')

# => Admin page
```

## or

```py
user = 'Admin'
logged_in = False # changed to false

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')

# => Admin page
```

## not

```py
if not logged_in:
    print('Please login...')
else:
    print('Welcome')
```

## is

**Object Identity**

```py
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # => True
print(a is b) # => False
print(id(a)) # => 2282773141824 (id in memory)
print(id(b)) # => 2282773139840 (id in memory)

b = a
print(a is b) # => True
print(id(a)) # => 1592589080896 (id in memory)
print(id(b)) # => 1592589080896 (id in memory)
```

# Falsy

```py
# * False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example: '', (), []
    # Any empty mapping (empty dictionary). For example: {}

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# => Evaluated to False
```

# Switch Case

**PYTHON DOES NOT HAVE SWITCH CASE**

Until version `3.12`, Python never had a feature that implemented what the switch statement does in other programming languages.
