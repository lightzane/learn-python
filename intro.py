language = 'Python'

# if True:
#     print('Conditional was True')

if language == 'Python':
    print('Conditional was True')

# * Comparisons
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Lesser or Equal:  <=
# Object Identity:  is

language = 'Typescript'

if language == 'Python':
    print('Language is Python')
    
elif language == 'Typescript':
    print('Language is Javascript with Typescript')

else:
    print('No match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad credentials')

logged_in = False

if not logged_in:
    print('Please login...')
else:
    print('Welcome')

# * is

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

# * False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example: '', (), []
    # Any empty mapping. For example: {}

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# => Evaluated to False